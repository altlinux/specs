Name: ssdeep
Url: http://ssdeep.sourceforge.net
License: GPL v2 or later
Group: Sciences/Mathematics
Version: 2.5
Release: alt1
Summary: Context Triggered Piecewise Hashing values
Source: http://dl.sourceforge.net/project/%name/%name-%version/%name-%version.tar.gz

%description
ssdeep is a program for computing and matching Context Triggered Piecewise
Hashing values. It is based on a spam detector called spamsum by Andrews
Trigdell

Authors:
--------
    Jesse Kornblum

See some examples here: http://www.forensicswiki.org/wiki/Ssdeep

%package -n libfuzzy
License: GPL v2 or later
Group: System/Libraries
Summary: Library that provides %summary

%description -n libfuzzy
Library that provides %summary, used by %name

%package -n libfuzzy-devel
License: GPL v2 or later
Group: Development/C
Summary: API for libfuzzy

%description -n libfuzzy-devel
API for libfuzzy, %summary

%package -n libfuzzy-devel-static
License: GPL v2 or later
Group: Development/C
Summary: API for %name
Requires: libfuzzy-devel = %version

%description -n libfuzzy-devel-static
Static library for libfuzzy, %summary

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%doc README COPYING FILEFORMAT
%_bindir/*
/usr/share/man/man1/*

%files -n libfuzzy
%_libdir/*.so.*

%files -n libfuzzy-devel
%_libdir/*.so
/usr/include/*

%files -n libfuzzy-devel-static
%_libdir/*.a

%changelog
* Tue Jul 13 2010 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- New version

* Tue Jul 13 2010 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Initial build from SuSE

