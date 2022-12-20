Name: rpm-build-tex
Version: 0.4.5
Release: alt1
Summary: RPM helper macros to rebuild TeX packages
License: %gpl3plus
Group: Development/Other
Source: %name-%version.tar
BuildArch: noarch
Requires: rpm >= 4.0.4-alt78
Url: http://git.altlinux.org/people/viy/packages/rpm-build-tex.git

BuildRequires(pre): rpm-build-licenses

Requires: tex-common
#Conflicts: tetex-core tetex tetex-latex tetex-dvips tetex-context tetex-afm

Provides: rpm-build-texmf = 0.4.0
Obsoletes: rpm-build-texmf < 0.4.0

%description
These helper macros provide possibility to rebuild TeX packages by
some Alt TeX Policy compatible way.

%prep
%setup


%install
install -d -m 0755 %buildroot{%_rpmlibdir,%_rpmmacrosdir}
install -m 0755 rpm/* %buildroot%_rpmlibdir/
install -m 0644 etc/* %buildroot%_rpmmacrosdir/


%files
%_rpmmacrosdir/*
%_rpmlibdir/tex.*


%changelog
* Tue Dec 20 2022 Igor Vlasenko <viy@altlinux.org> 0.4.5-alt1
- optimized tex.(req/prov).files (closes: #44643)

* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 0.4.4-alt1
- proper basename calls (closes: #43825)

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1
- cleaned up provides (closes: #36616)

* Mon Mar 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1
- add .tex provides

* Mon Mar 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- added clo,def,enc,ldf,bbx provides

* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2
- added conflicts on tetex

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- use new format of req/prov: tex(...) instead of texmf(...)
- renamed to rpm-build-tex

* Fri Nov 13 2009 Kirill Maslinsky <kirill@altlinux.org> 0.3.5-alt2
- fixed typo in %%_texmfsysconfig macro (thanks ldv@ for noticing)

* Tue Oct 27 2009 Kirill Maslinsky <kirill@altlinux.org> 0.3.5-alt1
- change req/prov search scope to TEXMF/tex/ subtree

* Sun Jun 28 2009 Kirill Maslinsky <kirill@altlinux.org> 0.3.4-alt1
- addded heuristic to detect and skip dependencies on conditionally 
  loaded latex packages

* Fri May 15 2009 Kirill Maslinsky <kirill@altlinux.org> 0.3.3-alt1
- tell about skipped requirements in verbose mode (bga@)

* Tue May 12 2009 Kirill Maslinsky <kirill@altlinux.org> 0.3.2-alt1
- added macro to skip listed requirements
  Usage: %%add_texmf_req_skip latex/foo

* Wed May 06 2009 Kirill Maslinsky <kirill@altlinux.ru> 0.3.1-alt1
- small fixes in req/prov code
- move rpm macros into %%_rpmmacrosdir
- require tex-common

* Tue Apr 28 2009 Kirill Maslinsky <kirill@altlinux.ru> 0.3.0-alt1
- new implementation (based on work by led@)

* Sat Sep 20 2008 Led <led@altlinux.ru> 0.2.0-alt1
- added latex.req*

* Sat Feb 23 2008 Led <led@altlinux.ru> 0.1.0-alt1
- initial build
