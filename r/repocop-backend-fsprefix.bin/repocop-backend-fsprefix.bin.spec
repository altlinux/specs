%define bname fsprefix.bin

Name: repocop-backend-%bname
Version: 0.004
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

for b in fssumbprefix.bin fssumxprefix.bin; do
    ln -s %bname %buildroot%_prefix/libexec/repocop/backends/$b
done

%files
#doc README ChangeLog
#%_bindir/repocop-*
%_prefix/libexec/repocop/backends/%bname
%_prefix/libexec/repocop/backends/fssumbprefix.bin
%_prefix/libexec/repocop/backends/fssumxprefix.bin

%changelog
* Wed Nov 22 2023 Igor Vlasenko <viy@altlinux.org> 0.004-alt1
- bugfix release

* Mon May 02 2022 Igor Vlasenko <viy@altlinux.org> 0.003-alt1
- bugfix release

* Thu Apr 28 2022 Igor Vlasenko <viy@altlinux.org> 0.002-alt1
- add fssumbprefix.bin and fssumxprefix.bin backends

* Mon Dec 27 2021 Igor Vlasenko <viy@altlinux.org> 0.001-alt1
- build for Sisyphus
