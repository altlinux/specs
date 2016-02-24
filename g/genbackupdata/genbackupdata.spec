Name: genbackupdata
Version: 1.9
Release: alt1

Summary: A program to generate test data for testing backup software

# upstream asked to include license text
License: GPLv2+
Group: Other
Url: http://liw.fi/%name/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://code.liw.fi/debian/pool/main/g/%name/%{name}_%version.orig.tar
Source44: import.info

BuildArch: noarch

# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# Automatically added by buildreq on Sat Aug 15 2015
# optimized out: python-base python-devel python-module-distribute python-module-oslo.i18n python-module-oslo.utils python-modules python-modules-compiler python-modules-email python-modules-logging python3-base
BuildRequires: python-module-cmd2 python-module-pycrypto

BuildRequires: python-devel
# END SourceDeps(oneline)

# build-time
BuildRequires: cmdtest
#BuildRequires: python-module-coverage-test-runner
# build- and run-time
BuildRequires: python-module-cliapp
BuildRequires: python-module-ttystatus

%description
genbackupdata creates or modifies directory trees in ways that
simulate real filesystems sufficiently well for performance testing of
backup software. For example, it can create files that are a mix of
small text files and big binary files, with the binary files
containing random binary junk which compresses badly. This can then be
backed up, and later the directory tree can be changed by creating new
files, modifying files, or deleting or renaming files. The backup can
then be run again.

The output is deterministic, such that for a given set of parameters
the same output always happens. Thus it is more efficient to
distribute genbackupdata and a set of parameters between people who
wish to benchmark backup software than distributing very large test
sets.

%prep
%setup

%build
%python_build
# build manpage
make genbackupdata.1

%install
%python_install

%check
exit 0
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
make check

%files
%doc NEWS README
%_man1dir/genbackupdata.1*
%_bindir/genbackupdata
%python_sitelibdir_noarch/*

%changelog
* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- new version 1.9 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- new version 1.8 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt4
- human build for ALT Linux Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_1
- update to new release by fcimport

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3
- initial fc import

