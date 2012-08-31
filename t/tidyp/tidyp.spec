Name: tidyp
Version: 1.04
Release: alt1

Summary: program that can validate your HTML, as well as modify it to be more clean and standard
License: W3C
Group: Text tools
Url: http://www.tidyp.com

# cloned from https://github.com/petdance/tidyp
Source: %name-%version.tar

%description
tidyp is a fork of tidy on SourceForge at http://tidy.sf.net.  The
library name is "tidyp", and the command-line tool is also "tidyp"
but all internal API stays the same.

tidyp will validate your HTML, and output cleaned-up HTML.

%package -n libtidyp
Summary: Shared libraries for tidyp
Group: System/Libraries

%description -n libtidyp
Shared libraries for tidyp.

%package -n libtidyp-devel
Summary: Development files for libtidyp
Group: Development/C
Requires: libtidyp = %{version}-%{release}

%description -n libtidyp-devel
Development files for libtidyp.

%prep
%setup -q

%build
touch NEWS COPYING AUTHORS
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/tidyp
%doc ChangeLog README

%files -n libtidyp
%_libdir/libtidyp-%version.so.0*

%files -n libtidyp-devel
%_includedir/tidyp
%_libdir/libtidyp.so
%exclude %_libdir/libtidyp.a

%changelog
* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1
- initial build

