# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: pkgconfig(python)
# END SourceDeps(oneline)
Name: btparser
Version: 0.17
Release: alt1_1
Summary: Parser and analyzer for backtraces produced by GDB
Group: Development/C
License: GPLv2+
URL: http://fedorahosted.org/btparser
Source0: https://fedorahosted.org/released/btparser/btparser-%{version}.tar.xz
BuildRequires: python-devel
Source44: import.info

%description
Btparser is a backtrace parser and analyzer, which works with
backtraces produced by the GNU Project Debugger. It can parse a text
file with a backtrace to a tree of C structures, allowing to analyze
the threads and frames of the backtrace and work with them.

Btparser also contains some backtrace manipulation and extraction
routines:
- it can find a frame in the crash-time backtrace where the program
  most likely crashed (a chance is that the function described in that
  frame is buggy)
- it can produce a duplication hash of the backtrace, which helps to
  discover that two crash-time backtraces are duplicates, triggered by
  the same flaw of the code
- it can "rate" the backtrace quality, which depends on the number of
  frames with and without the function name known (missing function
  name is caused by missing debugging symbols)

%package devel
Summary: Development libraries for %{name}
Group: Development/C
Requires: btparser = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%package -n python-module-btparser
Summary: Python bindings for %{name}
Group: Development/C
Requires: btparser = %{version}-%{release}

%description -n python-module-btparser
Python bindings for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove all libtool archives (*.la) from modules directory.
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%check
make check

%files
%doc README NEWS COPYING TODO ChangeLog
%{_bindir}/btparser
%{_mandir}/man1/%{name}.1.*
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files -n python-module-btparser
%dir %{python_sitelibdir}/%{name}
%{python_sitelibdir}/%{name}/*

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_1
- update to new release by fcimport

* Sat Nov 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- initial release by fcimport

