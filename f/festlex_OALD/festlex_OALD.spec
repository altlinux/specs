%define version	1.95
%define release	alt1

Name:		festlex_OALD
Version:	%{version}
Release:	%{release}
Group:		Sound
Copyright:	non-commercial and non-military use
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Oxford Advanced Learners' Dictionary for Festival
Requires:	festival
BuildArch:	noarch
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festlex_OALD.tar.gz

%description
Oxford Advanced Learners' Dictionary for Festival

%prep
%setup -q -c

%build

%install
DICT_DIR=$RPM_BUILD_ROOT/usr/share/festival/dicts

cd festival

install -d $DICT_DIR/oald
install -m 644 lib/dicts/oald/oald_lts_rules.scm $DICT_DIR/oald
install -m 644 lib/dicts/oald/oald-0.4.out $DICT_DIR/oald
install -m 644 lib/dicts/oald/oaldlex.scm $DICT_DIR/oald

%files
%defattr(-,root,root)
%doc festival/lib/dicts/oald/COPYING
/usr/share/festival/*

%changelog
* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- picked up from orphaned; spec cleanup

* Mon Nov 26 2001 Lev Levitin <lev@altlinux.ru>
  [festlex_OALD-1.4.1-alt2]
- Changed group to from Applications/Multimedia to Sound

* Thu Feb 15 2001 Lev Levitin <lev@mccme.ru>
  [festlex_OALD-1.4.1-alt1]
- Initial Mandrake RE release
