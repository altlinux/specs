Name: perl-Git-Raw
Version: 0.14
Release: alt1

Summary: Perl bindings to the Git linkable library (libgit2)
Group: Development/Perl
License: perl

Url: %CPAN Git-Raw
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libgit2-devel perl-base perl-Capture-Tiny perl-devel perl-File-Slurp perl-Devel-CheckLib

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Git/Raw*
%perl_vendor_archlib/Git/Raw*
%doc Changes TODO

%changelog
* Sun Oct 21 2012 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- 0.13 -> 0.14

* Wed Oct 10 2012 Buildbot <buildbot@altlinux.org> 0.13-alt1
- initial build for ALTLinux

