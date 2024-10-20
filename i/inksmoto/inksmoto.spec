Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-fedora-compat
# END SourceDeps(oneline)
# internal py
%filter_from_requires /^python3.inksmoto./d
%filter_from_requires /^python3.md5./d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: inksmoto
Version: 0.7.0
Release: alt2_32.1
Summary: The new xmoto level editor for Inkscape

License: GPL-2.0-only
URL: http://xmoto.sourceforge.net/
Source0: http://download.tuxfamily.org/xmoto/svg2lvl/%{version}~rc1/inksmoto-%{version}.tar.gz
BuildRequires: python3-devel
Requires: xmoto, inkscape, python3-module-lxml, python3-module-pygobject3
BuildArch: noarch

Patch0: inksmoto-0.7.0-pypath.patch
Patch1: inksmoto-python3.patch
Source44: import.info

%description
Inksmoto Level Editor is the new xmoto level editor. It uses Inkscape to
draw levels, then it allows you to save your drawing as a xmoto level
(.lvl file). It also allow you to edit xmoto level properties from 
within Inkscape such as make background block, strawberries, ...

Inksmoto Level Editor is written in Python, it's an Inkscape extension. 

%prep
%setup -qn extensions

%patch0 -p0
%patch1 -p1

%build
%python3_fix_shebang .

%install
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
rm -f bezmisc.py
rm -f inkex.py
cp -p *.inx *.py %{buildroot}%{_datadir}/inkscape/extensions/
chmod 644 %{buildroot}%{_datadir}/inkscape/extensions/*
cp -pr inksmoto %{buildroot}%{_datadir}/inkscape/extensions/


%files
%{_datadir}/inkscape/extensions/*
%doc --no-dereference COPYING
%doc AUTHORS INSTALL README

%changelog
* Thu Apr 11 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 0.7.0-alt2_32.1
- NMU: replace pathfix.py with %%python3_fix_shebang

* Thu Oct 12 2023 Igor Vlasenko <viy@altlinux.org> 0.7.0-alt2_32
- update to new release by fcimport

* Fri Dec 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_23
- python3 migration

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_21
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_18
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_15
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_10
- update to new release by fcimport

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_9
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- initial import by fcimport

