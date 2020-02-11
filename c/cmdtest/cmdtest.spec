Name: cmdtest
Version: 0.30
Release: alt2

Summary: Black-box testing for Unix command line tools
License: GPLv3+
Group: Development/Python3
Url: http://liw.fi/%name/
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: http://code.liw.fi/debian/pool/main/c/%name/%{name}_%version.orig.tar
Source44: import.info

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-markdown
BuildRequires: python3-module-cliapp
BuildRequires: python3-module-ttystatus


%description
cmdtest black box tests Unix command line tools. Roughly, it is given
a command line and input files, and the expected output, and it
verifies that the command line produces the expected output. If not,
it reports a problem, and shows the differences.

%prep
%setup

sed -i "s|'python'|'python3'|" setup.py

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%check
exit 0
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
%__python3 setup.py check

%files
%doc COPYING NEWS README README.yarn
%_bindir/cmdtest
%_bindir/yarn
%_man1dir/cmdtest.1*
%_man1dir/yarn.1*
%python3_sitelibdir_noarch/*


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.30-alt2
- Porting on python3.

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.30-alt1
- new version 0.30 (with rpmrb script)

* Sat Dec 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt1
- new version 0.27 (with rpmrb script)

* Sat Jan 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- new version 0.16 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt2
- human build for ALT Linux Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_1
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_1
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_4
- update to new release by fcimport

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 0.3-alt2_3
- rebuild to get rid of unmets

* Sat Jan 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_3
- initial fc import

