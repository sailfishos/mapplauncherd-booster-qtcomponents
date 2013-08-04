Name:       mapplauncherd-booster-qtcomponents-qt5
Summary:    Application launch booster for Qt5 Qt Components
Version:    0.0.0
Release:    1
Group:      System/Applications
License:    TBD
URL:        https://github.com/nemomobile/mapplauncherd-booster-qtcomponents
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  mapplauncherd-devel >= 4.1.0
BuildRequires:  pkgconfig(qdeclarative5-boostable)
Requires:  qt-components-qt5
Requires:  mapplauncherd >= 4.1.0

%description
Application launch booster for Qt5 Qt Components applications

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install

mkdir -p %{buildroot}%{_libdir}/systemd/user/user-session.target.wants/
ln -s ../booster-qtcomponents-qt5.service %{buildroot}/usr/lib/systemd/user/user-session.target.wants/

%files
%defattr(-,root,root,-)
%{_libexecdir}/mapplauncherd/booster-qtcomponents-qt5
%{_datadir}/booster-qtcomponents-qt5/*
%{_libdir}/systemd/user/booster-qtcomponents-qt5.service
%{_libdir}/systemd/user/user-session.target.wants/booster-qtcomponents-qt5.service

