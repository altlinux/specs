# with custom words added to this lex
%def_with custom

Name:		festlex_CMU
Version:	2.0.95
Release:	alt1
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	CMU Americal English Lexicon for Festival
Requires:	festival
BuildArch:	noarch
#Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festlex_CMU.tar.gz
Source0:http://festvox.org/packed/festival/2.0.95/festlex_CMU.tar.gz
#Source0:	http://www.speech.cs.cmu.edu/awb/fftest/festlex_CMU.tar.gz

# CMU-redhat.patch contains illegal sound ii1 :(
# %name-0.4-redhat-alt-fixed.patch is properly fixed CMU-redhat.
Patch0:		%name-0.4-redhat-alt-fixed.patch
Patch1:		%name-0.4-2.0.95-alt-Makefile.patch
%{?_with_custom:BuildRequires:	festival}

%description
American English Lexicon based on CMUDICT 0.4 and surround rules.

%prep
%setup -q -c
%if_with custom
%patch0 -p1
%patch1 -p1
%endif

%build
%if_with custom
pushd festival/lib/dicts/cmu
make ESTDIR=/
%endif

%install
DICT_DIR=$RPM_BUILD_ROOT/usr/share/festival/dicts

cd festival

install -d $DICT_DIR/cmu
install -m 644 lib/dicts/cmu/cmulex.scm $DICT_DIR/cmu
install -m 644 lib/dicts/cmu/cmu_lts_rules.scm $DICT_DIR/cmu
install -m 644 lib/dicts/cmu/cmudict-0.4.out $DICT_DIR/cmu

%clean

%files
%defattr(-,root,root)
/usr/share/festival/*

%changelog
* Wed Jul 07 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.95-alt1
- updated to http://festvox.org/packed/festival/2.0.95/ release

* Thu Dec 28 2006 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
- updated to latest awb test release

* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- picked up from orphaned; spec cleanup

* Sat Feb 3 2001 Lev Levitin <lev@mccme.ru>
  [festlex_CMU-1.4.1-ipl1mdk]
- Initial Mandrake RE release
