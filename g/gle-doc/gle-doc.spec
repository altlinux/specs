%define truename gle
Name: gle-doc
Version: 4.2.2
Release: alt1
Summary: Documentation for the GLE - Graphics language that produces ps/eps/pdf/png/jpg ouput
Summary(ru_RU.CP1251): GLE - язык создания изображений. Вывод в ps/eps/pdf/png/jpg
License: GPL2+
Packager: Igor Vlasenko <viy@altlinux.org>

Source4: http://dl.sourceforge.net/glx/gle-manual-4.2.2.pdf
Source5: http://dl.sourceforge.net/glx/GLEusersguide.pdf
URL: http://glx.sourceforge.net/

Group: Books/Computer books
BuildArch: noarch

%description
GLE is a graphics language that produces postscript, EPS, PDF, PNG, or JPG ouput from a simple script file. The GLE scripting language is full featured with variables, subroutines, logic control, looping, and graphing tools. It is great for plotting and charting data.

GLE can create very complex output with text and graphics (including graphs and charts) from a simple plain text file.

GLE is a full featured programing language that includes variables, subroutines, logic control, looping, a graphing tool, and more to produce high quality postscript output. It has a full range of facilities for producing publication-quality graphs, diagrams, posters and slides. GLE provides LaTeX quality fonts together with a flexible graphics module which allows the user to specify any feature of a graph (down to the line width of the subticks, for example). Complex pictures can be drawn with user-defined subroutines and simple looping structures. Essentially, GLE is a programming language and if you are used to writing software, using LaTeX, or any other non-WYSIWYG tools, then you will enjoy using GLE.

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

* Tue Jun 23 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt0.1
- first build for Sisyphus
