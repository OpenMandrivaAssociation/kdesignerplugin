%define major 5
%define debug_package %{nil}

Name: kdesignerplugin
Version: 5.3.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Integration of KDE Frameworks 5 widgets in Qt Designer/Creator
URL: http://kde.org/
License: GPL
Group: Development/KDE and Qt
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
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
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_bindir}/kgendesignerplugin
%{_libdir}/plugins/designer
%{_datadir}/kf5/widgets
%{_mandir}/man1/*
%{_libdir}/cmake/KF5DesignerPlugin
