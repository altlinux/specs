Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xa
Version:        2.3.14
Release:        alt1_1
Summary:        6502/65816 cross-assembler

License:        GPLv2+
URL:            http://www.floodgap.com/retrotech/xa/
Source0:        http://www.floodgap.com/retrotech/%{name}/dists/%{name}-%{version}.tar.gz
# update the build system, reported in private email
Patch0:         %{name}-2.3.7-make.patch
BuildRequires:  gcc
# Perl needed for test-suite
BuildRequires:  rpm-build-perl
Source44: import.info


%description
xa is a high-speed, two-pass portable cross-assembler. It understands
mnemonics and generates code for NMOS 6502s (such as 6502A, 6504, 6507,
6510, 7501, 8500, 8501, 8502 ...), CMOS 6502s (65C02 and Rockwell R65C02)
and the 65816.

Key amongst its features:

    * C-like preprocessor (and understands cpp for additional feature support)
    * rich expression syntax and pseudo-op vocabulary
    * multiple character sets
    * binary linking
    * supports o65 relocatable objects with a full linker and relocation suite, 
      as well as "bare" plain binary object files
    * block structure for label scoping 


%prep
%setup -q
%patch0 -p1


# fix encoding
for f in ChangeLog doc/fileformat.txt
do
    iconv -f ISO-8859-1 -t UTF-8 < $f > $f.new
    touch -r $f $f.new
    mv $f.new $f
done


%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"


%check
make test


%install
%makeinstall_std PREFIX=%{_prefix}


%files
%doc COPYING ChangeLog README.1st doc/fileformat.txt
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 2.3.14-alt1_1
- update to new release by fcimport

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.3.13-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.11-alt1_4
- update to new release by fcimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.11-alt1_2
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.10-alt1_2
- update to new release by fcimport

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt1_1
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt1_1
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_2
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.6-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_11
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_6
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_5
- initial release by fcimport

