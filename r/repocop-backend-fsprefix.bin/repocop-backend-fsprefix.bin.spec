%define bname fsprefix.bin

Name: repocop-backend-%bname
Version: 0.001
Release: alt1
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %bname backend for repocop test platform
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Url: http://repocop.altlinux.org
Requires: repocop > 0.82

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build
make

%install
install -D -m 755 repocop-test-ok %buildroot%_prefix/libexec/repocop/backends/%bname/repocop-test-ok
for i in  skip experimental info warn fail import-tsv; do
    ln -s repocop-test-ok %buildroot%_prefix/libexec/repocop/backends/%bname/repocop-test-$i
done

%files
#doc README ChangeLog
#%_bindir/repocop-*
%_prefix/libexec/repocop/backends/%bname

%changelog
* Mon Dec 27 2021 Igor Vlasenko <viy@altlinux.org> 0.001-alt1
- build for Sisyphus
