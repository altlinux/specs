# BEGIN SourceDeps(oneline):
BuildRequires: perl(JSON/XS.pm)
# END SourceDeps(oneline)
%define testname repology

Name: repocop-import-%testname
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname import unit tests for repocop test platform
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

%install
mkdir -p $RPM_BUILD_ROOT%_bindir/
install -m 755 \
   repocop-process-%testname \
   repocop-import-%testname \
   repocop-get-%testname \
   $RPM_BUILD_ROOT%_bindir/

for i in *.pl; do
    install -pD -m 755 $i %buildroot%_datadir/repocop/fixscripts/$i
done

%files
#doc README ChangeLog
%_bindir/repocop-*
%_datadir/repocop/fixscripts/*

%changelog
* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 0.03-alt1
- proper repocop import

* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.02-alt1
- mass report

* Sat Dec 18 2021 Igor Vlasenko <viy@altlinux.org> 0.01-alt1
- First build for Sisyphus.
