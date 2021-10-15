%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tidyp
Version: 1.04
Release: alt2
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
Requires: libtidyp = %EVR

%description -n libtidyp-devel
Development files for libtidyp.

%prep
%setup -q

%build
%add_optflags -D_FILE_OFFSET_BITS=64

touch NEWS COPYING AUTHORS
%autoreconf
%configure --disable-static
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

%changelog
* Fri Oct 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.04-alt2
- Fixed build with LTO

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1
- initial build

