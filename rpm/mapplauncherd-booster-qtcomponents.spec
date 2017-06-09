Name:       mapplauncherd-booster-qtcomponents
Summary:    Application launch booster for Qt Components
Version:    0.0.0
Release:    1
Group:      System/Applications
License:    LGPLv2.1
URL:        https://github.com/nemomobile/mapplauncherd-booster-qtcomponents
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(QtCore) >= 4.8.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(x11)
BuildRequires:  mapplauncherd-devel >= 4.1.0
BuildRequires:  pkgconfig(qdeclarative-boostable)
Requires:  qt-components
Requires:  mapplauncherd >= 4.1.0

%description
Application launch booster for Qt Components applications

%prep
%setup -q -n %{name}-%{version}

%build

%qmake 

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake_install

mkdir %{buildroot}/usr/lib/systemd/user/mapplauncherd.target.wants || true
ln -s ../booster-qtcomponents.service %{buildroot}/usr/lib/systemd/user/mapplauncherd.target.wants/

%files
%defattr(-,root,root,-)
%{_libexecdir}/mapplauncherd/booster-qtcomponents
%{_datadir}/booster-qtcomponents/*
%{_libdir}/systemd/user/booster-qtcomponents.service
%{_libdir}/systemd/user/mapplauncherd.target.wants/booster-qtcomponents.service

