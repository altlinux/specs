Name: rpm-build-texmf
Version: 0.3.5
Release: alt2
Summary: RPM helper macros to rebuild TeX packages
License: %gpl3plus
Group: Development/Other
Source: %name-%version.tar
BuildArch: noarch
Requires: rpm >= 4.0.4-alt78
Packager: Kirill Maslinsky <kirill@altlinux.org>
Url: http://git.altlinux.org/people/kirill/packages/rpm-build-texmf.git

BuildRequires(pre): rpm-build-licenses

Requires: tex-common

Provides: rpm-build-tex <= 0.2.0
Obsoletes: rpm-build-tex <= 0.2.0

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
%_rpmlibdir/texmf.*


%changelog
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
