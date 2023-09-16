Name: gle-doc
Version: 4.3.4
Release: alt1
Summary: Documentation for the GLE - Graphics language that produces ps/eps/pdf/png/jpg ouput
Summary(ru_RU.UTF-8): GLE - язык создания изображений. Вывод в ps/eps/pdf/png/jpg
License: GPLv2+
Packager: Igor Vlasenko <viy@altlinux.org>

Source4: gle-manual-4.3.4.pdf
Source5: http://dl.sourceforge.net/glx/GLEusersguide.pdf
URL: http://glx.sourceforge.io/


Group: Books/Computer books
BuildArch: noarch

%description
GLE is a graphics language that produces postscript, EPS, PDF, PNG, or JPG ouput
from a simple script file. The GLE scripting language is full featured with variables,
subroutines, logic control, looping, and graphing tools.
It is great for plotting and charting data.

GLE can create very complex output with text and graphics (including graphs and charts)
from a simple plain text file.

This package contains documentation.

%prep
%setup -q -T -c

%build
cp %{SOURCE5} %{SOURCE4} .

%install
mkdir $RPM_BUILD_ROOT

%files
%doc [gG][lL][eE]-*manual*.pdf GLEusersguide.pdf

%changelog 
* Sat Sep 16 2023 Igor Vlasenko <viy@altlinux.org> 4.3.4-alt1
- new version of manual

* Tue Feb 21 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.4-alt2
- UTF-8 in summary

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.4-alt1
- new version of manual

* Thu Feb 11 2010 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1
- new version of manual

* Mon Apr 13 2009 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- new version of manual

* Sun Aug 10 2008 Igor Vlasenko <viy@altlinux.ru> 4.0.13-alt1
- new version of manual

* Tue Jul 10 2007 Igor Vlasenko <viy@altlinux.ru> 4.0.12-alt1
- new version of manual (pre1)

* Thu Jan 05 2006 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt3
- fixed arch to be noarch

* Mon Dec 26 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt2
- split gle and gle-doc. 
  gle-doc is updated less frequent and asynchronically with gle,
  so this split will considerably reduce gle traffic.

* Fri Dec 23 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1
- new version

* Mon Nov 21 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.10-alt2
- gle-manual updated

* Wed Nov 16 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.10-alt1
- new version

* Tue Sep 27 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.9-alt2
- utils moved from _datadir to _libdir

* Fri Aug 26 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.9-alt1
- new version
