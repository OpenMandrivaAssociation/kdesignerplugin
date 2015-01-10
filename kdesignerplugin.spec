%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdesignerplugin
Version: 5.6.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Integration of KDE Frameworks 5 widgets in Qt Designer/Creator
URL: http://kde.org/
License: GPL
Group: Development/KDE and Qt
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: qt5-designer
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
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
BuildRequires: cmake(KF5WebKit)
BuildRequires: ninja

%description
Integration of KDE Frameworks 5 widgets in Qt Designer/Creator

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_bindir}/kgendesignerplugin
%{_libdir}/qt5/plugins/designer/*
%{_datadir}/kf5/widgets
%{_libdir}/cmake/KF5DesignerPlugin
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*
%lang(sv) %{_mandir}/sv/man1/*
%lang(uk) %{_mandir}/uk/man1/*
