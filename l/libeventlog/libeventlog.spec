%define real_name eventlog
%def_disable static

Name: lib%real_name
Version: 0.2.9
Release: alt3

Summary: The EventLog library implements a set of functions for handle event records.
License: distributable
Group: System/Libraries
Url: http://www.balabit.com/network-security/syslog-ng/

Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Source: http://www.balabit.com/downloads/files/eventlog/0.2/%real_name-%version.tar.bz2

%description
The EventLog library implements a set of functions to construct, format and
output event records. It is needed to build syslog-ng-2.0 the new generation
syslog.

%package devel
Group: Development/C
License: distributable
Summary: Development environment for %name
Requires: %name = %version-%release

%description devel
This package contains development files required to build
%name-based software.

%package devel-static
Group: Development/C
License: distributable
Summary: Static %name library
Requires: %name-devel = %version-%release

%description devel-static
This package contains static library required to build
statically linked %name-based software.

%prep
%setup -q -n %real_name-%version

%build
%configure %{subst_enable static}

%make_build

%install
%makeinstall

#relocate library to %_lib from %_libdir
for f in %buildroot/%_libdir/*.so; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	%__ln_s -nf ../../%_lib/"$t" "$f"
done
%__mkdir_p %buildroot/%_lib
%__mv %buildroot/%_libdir/*.so.* %buildroot/%_lib/

%files
/%_lib/*so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt3
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt2
- Rebuilt for soname set-versions

* Sun Jan 11 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.2.9-alt1
- 0.2.9

* Thu Jan 10 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Tue Oct 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.2.5-alt1
- relocate library from /usr/{lib,lib64} to /{lib,lib64}

* Tue Jan 09 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 0.2.5-alt0
- initial release

