%define oldname libstatgrab
Name: libstatgrab6
Version: 0.17
Release: alt1.2

Summary: libstatgrab library helps to collect many system infomation
License: LGPL, GPL
Group: System/Legacy libraries

Url: http://www.i-scream.org/libstatgrab/
Source: %oldname-%version.tar.gz
Patch: %oldname-alt-makefile.patch
Packager: Sergey Zhumatiy <zhum@altlinux.org>

%description
Statgrab is a crossplatform library to collect system information.
Such as loadaverage, cpu usage, network usage, memory usage, etc.

%package tools
Summary: Console program to check system activity
Group: Monitoring
Requires: %{name} = %version-%release

%description tools
Console program to check system activity, using libstatgrab.

%package saidar
Summary: Console program to check system activity
Group: Monitoring
Requires: libncurses
Requires: %{name} = %version-%release
BuildRequires: libncurses-devel

%description saidar
Console program to check system activity, using libstatgrab.

%package devel
Summary: Headers for %oldname
Group: Development/C
Requires: %{name} = %version-%release

%description devel
Headers for building software that uses %oldname
%if_enabled static
%package devel-static
Summary: Static libraries for %oldname
Group: Development/C
Requires: %{name}-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %oldname
%endif

%prep
%setup -n %{oldname}-%{version}
%patch -p1

%build
%configure --with-ncurses %{subst_enable static}
#%%configure --disable-saidar %{subst_enable static}
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
#%%make_build
make DESTDIR=$RPM_BUILD_ROOT

%install
%makeinstall
#make DESTDIR=$RPM_BUILD_ROOT install

%files
%_libdir/*.so.*
#%%_libdir/*.la
#%_libdir/%oldname.a
%doc AUTHORS README NEWS

%if 0
%files saidar
%_bindir/saidar
%_man1dir/saidar.1*

%files tools
#%%_bindir/saidar
%_bindir/statgrab
%_bindir/statgrab-make-mrtg-config
%_bindir/statgrab-make-mrtg-index
%_man1dir/statgrab-make-mrtg-config.1*
%_man1dir/statgrab-make-mrtg-index.1*
%_man1dir/statgrab.1*

%files devel
%_libdir/*.so
%_includedir/*.h
%_man3dir/*
%_libdir/pkgconfig/libstatgrab.pc
#%%_mandir/*/*
%endif

#%%if_enabled static
#%%files -n %oldname-devel-static
#
#%%endif

%changelog
* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.2
- compat library

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.1
- Removed bad RPATH

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 0.17-alt1
- NMU: 0.17 (thx fedorawatch)

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.qa1.1
- Rebuilt for soname set-versions

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.16-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libstatgrab
  * postun_ldconfig for libstatgrab
  * postclean-05-filetriggers for spec file

* Mon May 25 2009 Sergey Zhumatiy <zhum@altlinux.org> 0.16-alt1
- fixed wrong pkgconfig file location on x86_64 (spec file bug)
- new version 0.16
- saidar is added as separated package

* Thu Nov 15 2007 Sergey Zhumatiy <zhum@altlinux.org> 0.14-alt3
- saidar deleted from package because of unstable compiling

* Fri Oct 19 2007 Sergey Zhumatiy <zhum@altlinux.org> 0.14-alt2
- main pakage is splitted to libstatgrab and libstatgrab-tools

* Fri Oct 05 2007 Sergey Zhumatiy <zhum@altlinux.org> 0.14-alt1
- initial build

