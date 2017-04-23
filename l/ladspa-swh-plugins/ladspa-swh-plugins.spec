%define _name swh-plugins
%def_disable system_ladspa
%ifarch %ix86 x86_64
%def_enable sse
%endif

Name: ladspa-%_name
Version: 0.4.17
Release: alt1

Summary: A set of audio plugins for LADSPA
Summary(ru_RU.UTF-8): Набор модулей LADSPA от Стива Хэрриса и сотоварищей
Group: Sound
License: GPL
Url: http://plugin.org.uk

# VCS: https://github.com/swh/ladspa.git
Source: ladspa-%version.tar.gz
#Source: %url/releases/%version/%_name-%version.tar.gz
Source1: %url/ladspa-swh/docs/ladspa-swh.html

%define ladspa_ver 1.13

PreReq: ladspa_sdk >= %ladspa_ver

BuildPreReq: ladspa_sdk >= %ladspa_ver

BuildRequires: ladspa_sdk libfftw3-devel perl-XML-Parser

%description
A set of Steve Harris' audio plugins for LADSPA (Linux
Audio Developer's Simple Plugin Architecture).

%prep
%setup -n ladspa-%version
%if_enabled system_ladspa
rm -f ladspa.h
find . -type f -print0|xargs -r0 subst 's,"ladspa.h",<ladspa.h>,' --
%endif

%build
%add_optflags %optflags_shared
%autoreconf
%configure %{subst_enable sse}
%make_build plugindir=%_ladspa_path

%install
%makeinstall_std

cp gsm/README README.gsm
cp %SOURCE1 .

%find_lang %_name

%files -f %_name.lang
%_ladspa_path/*.so
%_ladspa_datadir/rdf/*
%doc AUTHORS README ChangeLog README.gsm ladspa-swh.html

%changelog
* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.17-alt1
- 0.4.17

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.11-alt3.qa1
- NMU: rebuilt for debuginfo.

* Thu Aug 27 2009 Damir Shayhutdinov <damir@altlinux.ru> 0.4.11-alt3
- Fix BuildReq

* Sun Feb 04 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.4.11-alt2
- Fix build on modern Sisyphus

* Tue Nov 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.11-alt1
- 0.4.11

* Fri Aug 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.7-alt1.1
- fixed buildreqs.

* Sun Jul 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.7-alt1
- 0.4.7 

* Thu Jun 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.4-alt1
- 0.4.4

* Wed Dec 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Tue Oct 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt3
- fixed %%build

* Tue Jun 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt2
- rebuild with FFTW3.

* Mon Jun 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Tue Apr 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sat Mar 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.7-alt1
- 0.3.7

* Fri Jan 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Sat Dec 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Thu Dec 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Tue Dec 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Nov 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Tue Sep 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.8-alt1
- 0.2.8 

* Sat May 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.5-alt1
- 0.2.5 

* Mon Jan 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt1
- new version
- cleanups

* Sat Jan 5 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.2-alt1
- Updated to 0.2.2

* Fri Nov 23 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt1
- First build for Sisyphus
