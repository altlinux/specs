# BEGIN SourceDeps(oneline):
BuildRequires: python-devel
# END SourceDeps(oneline)
Name: inksmoto
Version: 0.7.0
Release: alt2_14
Summary: The new xmoto level editor for Inkscape

Group: Games/Other
License: GPLv2
URL: http://xmoto.sourceforge.net/
Source0: http://download.tuxfamily.org/xmoto/svg2lvl/%{version}~rc1/inksmoto-%{version}.tar.gz
Requires: xmoto, inkscape, python-module-lxml, pygtk2
BuildArch: noarch

Patch0: inksmoto-0.7.0-pypath.patch
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

%build

%install
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions
rm -f bezmisc.py
rm -f inkex.py
cp -p *.inx *.py %{buildroot}%{_datadir}/inkscape/extensions/
chmod 644 %{buildroot}%{_datadir}/inkscape/extensions/*
cp -pr inksmoto %{buildroot}%{_datadir}/inkscape/extensions/

%files
%{_datadir}/inkscape/extensions/*
%doc AUTHORS COPYING INSTALL README

%changelog
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

