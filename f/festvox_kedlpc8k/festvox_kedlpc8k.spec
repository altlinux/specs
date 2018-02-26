%define version	1.95
%define release	alt1

Name:		festvox_kedlpc8k
Version:	%{version}
Release:	%{release}
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: American English male speaker (8KHz sampling)
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
BuildArch:	noarch

Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_kedlpc8k.tar.gz

%description
American English male speaker using residual excited LPC diphone database
at 8KHz sampling.

%prep
%setup -q -c

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT/usr/share/festival/voices

cd festival

install -d $VOICE_DIR/english/ked_diphone/festvox
install -d $VOICE_DIR/english/ked_diphone/group
install -m 644 lib/voices/english/ked_diphone/festvox/* $VOICE_DIR/english/ked_diphone/festvox
install -m 644 lib/voices/english/ked_diphone/group/* $VOICE_DIR/english/ked_diphone/group

%files
/usr/share/festival/*

%changelog
* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- picked up from orphaned; spec cleanup

* Sat Feb 3 2001 Lev Levitin <lev@mccme.ru>
  [festlex_POSLEX-1.4.1-ipl1mdk]
- Initial Mandrake RE release
  
