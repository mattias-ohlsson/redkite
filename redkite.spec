Name:           redkite
Version:        0.6.3
Release:        3%{?dist}
Summary:        A small software GUI toolkit

License:        GPLv3+
URL:            https://gitlab.com/geontime/redkite
Source0:        https://github.com/geontime/%{name}/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cairo-devel

%description
Redkite is a small free software GUI toolkit. It is developed in C++17 and
inspired from other well known GUI toolkits.

%package -n %{name}-devel
Summary: Files needed for building applications with %{name}
Requires: %{name} = %{version}-%{release}

%description -n %{name}-devel
The %{name}-devel package includes header files and libraries necessary for
developing programs which use the %{name} library.

%prep
%autosetup

%build
mkdir build
cd build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} ../
%make_build

%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/rkpng2c

%files -n %{name}-devel
%{_libdir}/lib%{name}.a
%{_includedir}/%{name}/*.h

%changelog
* Fri Jan 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.6.3-1
- Initial build
