Summary: Library that parses MXP stream
Name:    libmxp
Version: 0.2.4
Release: alt2
License: LGPLv2+
Group:   System/Libraries 
Url:     http://www.kmuddy.com

Source0: %name-%version.tar.gz

BuildRequires: gcc-c++ cmake

%description
Library that parses MXP stream.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version

%description devel 
This package contains files need to build applications using libmxp.

%prep
%setup -q

%build
%cmake
cd BUILD
%make

%install
cd BUILD
%makeinstall_std

%files 
%_libdir/*.so.0*

%files devel
%doc ChangeLog README* NEWS
%_libdir/*.so
%_includedir/*


%changelog
* Tue Aug 30 2011 Andrey Cherepanov <cas@altlinux.org> 0.2.4-alt2
- Rebuild for kmuddy changes

* Thu Feb 03 2011 Andrey Cherepanov <cas@altlinux.org> 0.2.4-alt1
- Initial build in Sisyphus

