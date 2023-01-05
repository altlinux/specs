# BEGIN SourceDeps(oneline):
BuildRequires: hasher
# END SourceDeps(oneline)
Name: hsh-clone-workdir
Version: 0.004
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: scripts to clone and re-initialize hasher workdir
Group: Development/Other
License: GPLv2+
Url: https://www.altlinux.org/Autorepo
Source: %name-%version.tar

Requires: hasher

%description
%summary

hsh-initroot fork is rebased against hasher 1.6.1

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
install -m 755 bin/hsh-* $RPM_BUILD_ROOT%_bindir/

%files
%_bindir/hsh*

%changelog
* Thu Jan 05 2023 Igor Vlasenko <viy@altlinux.org> 0.004-alt1
- hsh-initroot fork rebased against hasher 1.6.1

* Fri Jul 08 2022 Igor Vlasenko <viy@altlinux.org> 0.003-alt1
- Sisyphus release

* Sat Sep 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- hsh-initroot fork rebased against hasher 1.4.4

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version

