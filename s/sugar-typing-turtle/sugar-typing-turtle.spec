# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: gcc-c++ pkgconfig(gtk+-2.0) pkgconfig(x11) python-devel
# END SourceDeps(oneline)
Name:           sugar-typing-turtle
Version:        29
Release:        alt1_2
Summary:        A multilingual animated touch typing trainer

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Typing_Turtle
Source0:        http://activities.sugarlabs.org/sugar/downloads/file/26483/typing_turtle-%{version}.xo

BuildArch:      noarch
BuildRequires:  sugar-toolkit
BuildRequires:  gettext
Requires:       sugar
Source44: import.info

%description
This Sugar activity features a sequence of lessons designed to gradually
introduce students to touch typing, teaching them a few keys at a time
until they have mastered the entire keyboard.

Fun graphics, sounds and characters aim for an entertaining experience.
An on-screen keyboard with overlaid hand positions shows the correct way
to press each key, encouraging good typing habits.


%prep
%setup -q -n TypingTurtle.activity

# remove unnecessary libs and files
rm -rf .pydevproject .project strace.sh

# resolve license file naming issues
mv port/COPYING port/COPYING-port

# calm rpmlint down and fix permissions
sed -i -e '1d;2i#!/usr/bin/python' typingturtle.py
sed -i -e '/^#!\//, 1d' editlessonscreen.py editlessonlistscreen.py

%build
python setup.py build


%install
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.community.TypingTurtle


%files -f org.laptop.community.TypingTurtle.lang
%doc port/COPYING-port COPYING NEWS
%{sugaractivitydir}/TypingTurtle.activity


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 29-alt1_2
- new version; import from fc17 updates

