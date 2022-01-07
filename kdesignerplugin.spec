%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdesignerplugin
Version:	5.90.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: Integration of KDE Frameworks 5 widgets in Qt Designer/Creator
URL: http://kde.org/
License: GPL
Group: Development/KDE and Qt
BuildRequires: cmake(ECM)
BuildRequires: qt5-designer
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Designer)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Plotting)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5WebKit) >= %{version}
# cmake files act up when running into obsolete-ish Qt5Declarative
BuildConflicts:	pkgconfig(Qt5Declarative)

%description
Integration of KDE Frameworks 5 widgets in Qt Designer/Creator.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

L="$(pwd)/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
    LNG=$(echo $i |cut -d/ -f5)
    echo -n "%lang($LNG) " >>$L
    echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_bindir}/kgendesignerplugin
%{_libdir}/cmake/KF5DesignerPlugin
%{_mandir}/man1/*
%lang(ca) %{_mandir}/ca/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pt) %{_mandir}/pt/man1/*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*
%lang(sv) %{_mandir}/sv/man1/*
%lang(uk) %{_mandir}/uk/man1/*
