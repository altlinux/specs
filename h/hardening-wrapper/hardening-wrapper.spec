# This is intentional to see, if the tool correctly
# detects diffs in hardening during %%check.
%global _hardened_build 0

# The resulting binary-package is noarch'ed, so there
# is no useful debuginfo generated during build.  We
# just build the empty main-package archful to run the
# testsuite on all available arches.
%global debug_package %nil

Name: hardening-wrapper
Version: 2.6
Release: alt1

Summary: Tool to check ELF for being built hardened
License: GPLv2+
Group: Development/Tools

Url: http://packages.debian.org/%name
Source: http://ftp.debian.org/debian/pool/main/h/%name/%{name}_%version.tar.xz
Patch: %name-2.6-fix_perl.patch

BuildArch: noarch
BuildRequires: rpm-build-perl
BuildRequires: perl-podlators

%description
hardening-check is a tool to check whether an already compiled ELF file
was built using hardening flags.

It checks, using readelf, for these hardening characteristics:

  * Position Independent Executable
  * Stack protected
  * Fortify source functions
  * Read-only relocations
  * Immediate binding

%package -n hardening-check
Summary: Tool to check ELF for being built hardened
Group: Development/Tools
Requires: binutils

%description -n hardening-check
hardening-check is a tool to check whether an already compiled ELF file
was built using hardening flags.

It checks -- using readelf -- for these hardening characteristics:

  * Position Independent Executable
  * Stack protected
  * Fortify source functions
  * Read-only relocations
  * Immediate binding

%prep
%setup -c
%patch -p1

# Remove debian-specific checks from Makefile.
sed -i.debian -e '/^[ \t]*if \[ -z \"\$.DEB_/d' \
	%name/Makefile

%build
%make_build -C %name

%install
install -pDm0755 %name/build-tree/hardening-check \
	%buildroot%_bindir/hardening-check
install -pDm0644 %name/build-tree/hardening-check.1 \
	%buildroot%_mandir/man1/hardening-check.1

%check
%make_build -C %name check

%files -n hardening-check
%doc %name/TODO
%doc %name/debian/README.Debian
%doc %name/debian/changelog
%doc %name/AUTHORS
%doc %name/debian/copyright
%_bindir/hardening-check
%_man1dir/hardening-check.1.*

%changelog
* Fri Apr 19 2019 Michael Shigorin <mike@altlinux.org> 2.6-alt1
- adapted from fedora
