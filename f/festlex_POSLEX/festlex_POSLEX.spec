%define version	1.95
%define release	alt1

Name:		festlex_POSLEX
Version:	%{version}
Release:	%{release}
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Lexicon for English part of speech tagging
Requires:	festival
BuildArch:	noarch

Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festlex_POSLEX.tar.gz

%description
Lexicon for English part of speech tagging

%prep
%setup -q -c

%build

%install
DICT_DIR=$RPM_BUILD_ROOT/usr/share/festival/dicts

cd festival

install -d $DICT_DIR
install -m 644 lib/dicts/wsj.wp39.poslexR $DICT_DIR
install -m 644 lib/dicts/wsj.wp39.tri.ngrambin $DICT_DIR

%clean

%files
%defattr(-,root,root)
/usr/share/festival/*

%changelog
* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- picked up from orphaned; spec cleanup

* Sat Feb 3 2001 Lev Levitin <lev@mccme.ru>
  [festlex_POSLEX-1.4.1-ipl1mdk]
- Initial Mandrake RE release
