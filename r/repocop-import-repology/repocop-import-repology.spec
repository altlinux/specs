# BEGIN SourceDeps(oneline):
BuildRequires: perl(JSON/XS.pm)
# END SourceDeps(oneline)
%define testname repology

Name: repocop-import-%testname
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname import unit tests for repocop test platform
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Url: http://repocop.altlinux.org
Requires: repocop >= 0.80

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_bindir/
install -m 755 \
   repocop-import-%testname \
   repocop-get-%testname \
   $RPM_BUILD_ROOT%_bindir/

for i in *.pl; do
    install -pD -m 755 $i %buildroot%_datadir/repocop/fixscripts/$i
done

mkdir -p %buildroot%_datadir/repocop/srctests/%testname/
    ln -s ../../../../bin/repocop-import-%testname \
    %buildroot%_datadir/repocop/srctests/%testname/posttest

%files
#doc README ChangeLog
%_bindir/repocop-*
%_datadir/repocop/fixscripts/*
%_datadir/repocop/srctests/*

%changelog
* Sat Dec 18 2021 Igor Vlasenko <viy@altlinux.org> 0.01-alt1
- First build for Sisyphus.
