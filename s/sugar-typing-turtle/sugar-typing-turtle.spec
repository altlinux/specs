# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-typing-turtle
Version:        30
Release:        alt1_2
Summary:        A multilingual animated touch typing trainer

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Typing_Turtle
Source0:        http://download.sugarlabs.org/sources/honey/TypingTurtle/TypingTurtle-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
Requires:       sugar >= 0.97.0
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
This Sugar activity features a sequence of lessons designed to gradually
introduce students to touch typing, teaching them a few keys at a time
until they have mastered the entire keyboard.

Fun graphics, sounds and characters aim for an entertaining experience.
An on-screen keyboard with overlaid hand positions shows the correct way
to press each key, encouraging good typing habits.


%prep
%setup -q -n TypingTurtle-%{version}

# remove unnecessary libs and files
rm -rf .pydevproject .project strace.sh

# calm rpmlint down and fix permissions
sed -i -e '1d;2i#!/usr/bin/python' typingturtle.py
sed -i -e '/^#!\//, 1d' editlessonscreen.py editlessonlistscreen.py

%build
python ./setup.py build

%install
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.community.TypingTurtle


%files -f org.laptop.community.TypingTurtle.lang
%doc COPYING NEWS
%{sugaractivitydir}/TypingTurtle.activity


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 30-alt1_2
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 29-alt1_2
- new version; import from fc17 updates

