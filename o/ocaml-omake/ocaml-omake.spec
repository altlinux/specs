Name:           ocaml-omake
Version:        0.9.8.6
Release:        alt1%ubt
Summary:        Build system with automated dependency analysis
License:        LGPLv2+ with exceptions and GPLv2+ and BSD
Group:          Development/ML

URL:            http://omake.metaprl.org/download.html
Source: 	%name-%version.tar

Patch0:         omake-debian-disable-ocaml-warnings.patch
Patch1:         omake-0.9.8.6-fix-and-or-operators.patch
Patch2:         omake-0.9.8.6-kill-warn-error.patch

BuildRequires: rpm-build-ocaml ocaml
BuildRequires(pre):rpm-build-ubt
Provides: ocaml4-omake = %version-%release
Obsoletes: ocaml4-omake

%description
OMake is a build system designed for scalability and portability. It
uses a syntax similar to make utilities you may have used, but it
features many additional enhancements, including the following.

 * Support for projects spanning several directories or directory
   hierarchies.

 * Fast, reliable, automated, scriptable dependency analysis using MD5
   digests, with full support for incremental builds.

 * Dependency analysis takes the command lines into account - whenever
   the command line used to build a target changes, the target is
   considered out-of-date.

 * Fully scriptable, includes a library that providing support for
   standard tasks in C, C++, OCaml, and LaTeX projects, or a mixture
   thereof.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make all \
  PREFIX=%{_prefix} MANDIR=%{_mandir} BINDIR=%{_bindir} LIBDIR=%{_libdir}


%install
make install \
  INSTALL_ROOT=$RPM_BUILD_ROOT \
  PREFIX=%{_prefix} MANDIR=%{_mandir} BINDIR=%{_bindir} LIBDIR=%{_libdir}

chmod 0755 $RPM_BUILD_ROOT%{_bindir}/*

%files
%doc LICENSE LICENSE.OMake
%doc CHANGELOG.txt
%doc doc/txt/omake-doc.txt doc/ps/omake-doc.pdf doc/html/
%dir %_libdir/omake/
%_libdir/omake/*
%_bindir/omake
%_bindir/osh
%_bindir/cvs_realclean

%changelog
* Sun Apr 16 2017 Anton Farygin <rider@altlinux.ru> 0.9.8.6-alt1%ubt
- renamed to ocaml-omake
- built with new ocaml-4.04

* Tue Jun 23 2015 Andrey Bergman <vkni@altlinux.org> 0.9.8.6-alt0.1
- Initial release for Sisyphus.

