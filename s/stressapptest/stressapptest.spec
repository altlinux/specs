Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires: libaio-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 6

%global forgeurl https://github.com/stressapptest/stressapptest
%global commit 6714c57d0d67f5a2a7a9987791af6729289bf64e
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/stressapptest/stressapptest
%global forgesource https://github.com/stressapptest/stressapptest/archive/6714c57d0d67f5a2a7a9987791af6729289bf64e/stressapptest-6714c57d0d67f5a2a7a9987791af6729289bf64e.tar.gz
%global archivename stressapptest-6714c57d0d67f5a2a7a9987791af6729289bf64e
%global archiveext tar.gz
%global archiveurl https://github.com/stressapptest/stressapptest/archive/6714c57d0d67f5a2a7a9987791af6729289bf64e/stressapptest-6714c57d0d67f5a2a7a9987791af6729289bf64e.tar.gz
%global topdir stressapptest-6714c57d0d67f5a2a7a9987791af6729289bf64e
%global extractdir stressapptest-6714c57d0d67f5a2a7a9987791af6729289bf64e
%global repo stressapptest
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 6714c57d0d67f5a2a7a9987791af6729289bf64e
#global shortcommit %nil
#global branch %nil
%global version 1.0.9
#global date %nil
%global distprefix .git6714c57
# FedoraForgeMeta2ALT: end generated meta

Name:           stressapptest
Version:        1.0.9
Release:        alt1_%autorelease
Summary:        Stressful Application Test - userspace memory and IO test

License:        ASL 2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
Source44: import.info

%description
Stressful Application Test (or stressapptest, its unix name) is a memory
interface test. It tries to maximize randomized traffic to memory from
processor and I/O, with the intent of creating a realistic high load situation
in order to test the existing hardware devices in a computer. It has been used
at Google for some time and now it is available under the Apache 2.0 license.

%prep
%setup -q -n stressapptest-6714c57d0d67f5a2a7a9987791af6729289bf64e

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc --no-dereference COPYING NOTICE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Oct 24 2024 Igor Vlasenko <viy@altlinux.org> 1.0.9-alt1_6
- new version

