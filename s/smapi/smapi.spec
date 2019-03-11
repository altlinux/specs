%define reldate 20190311
%define reltype C
# may be one of: C (current), R (release), S (stable)

%if %_vendor == "alt"
%define pkg_group Networking/FTN
%define mnt_mail gremlin@altlinux.org
%else
%define pkg_group Libraries/FTN
%define mnt_mail 2:5020/545
%endif

Name: smapi
Version: 2.5.%{reldate}%{reltype}
Release: %{_vendor}1
Group: %pkg_group
Summary: Squish/Jam API for the Husky Project applications
URL: https://github.com/huskyproject/huskylib
License: GPL
Source: %{name}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: huskylib-devel-libs-shared huskylib-devel-libs-static
BuildRequires: glibc-devel-static

%description
%summary

%package devel
Group: %pkg_group
Summary: Development headers for %name
BuildArch: noarch
Requires: %name-devel-libs = %version-%release

%description devel
%summary


%package devel-libs-shared
Summary: Shared development libraries for %name
Group: %pkg_group
Requires: %name-devel = %version-%release
Requires: %name = %version-%release
Provides: %name-devel-libs = %version-%release

%description devel-libs-shared
%summary


%package devel-libs-static
Summary: Static development libraries for %name
Group: %pkg_group
Requires: %name-devel = %version-%release
Provides: %name-devel-libs = %version-%release

%description devel-libs-static
%summary



%prep
%setup -q -n %{name}
date '+char cvs_date[]="%%F";' > cvsdate.h

%build
%make DYNLIBS=1
%make


%install
rm -rf -- %buildroot
umask 022
make DESTDIR=%buildroot DYNLIBS=1 install
make DESTDIR=%buildroot install
chmod -R a+rX,u+w,go-w %buildroot


%clean
rm -rf -- %buildroot


%files
%defattr(-,root,root)
%_libdir/*.so.*

%files devel
%dir %_includedir/%name
%_includedir/%name/*

%files devel-libs-shared
%_libdir/*.so

%files devel-libs-static
%_libdir/*.a

%changelog
* Mon Mar 11 2019 Gremlin from Kremlin <%{mnt_mail}> 2.5.20190311C-%{_vendor}1
- rewrite .spec from scratch, split to subpackages
