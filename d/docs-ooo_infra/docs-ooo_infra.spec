Name: docs-ooo_infra
Version: 0.1
Release: alt2

Group: Books/Other
Packager: ALT Docs Team <docs@packages.altlinux.org>
Summary: Set of OpenOffice.org guides (virtual package)
License: %gpl2plus
Buildarch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: docs-ooo_infra_writer_guide
Requires: docs-ooo_infra_calc_guide
Requires: docs-ooo_infra_impress_guide
Requires: docs-ooo_infra_draw_guide

# docs-openoffice-kirill-060324-alt2 obsoletes alt-docs-extras-openoffice
# so we obsolete both: docs-openoffice-kirill, alt-docs-extras-openoffice
Obsoletes: docs-openoffice-kirill, alt-docs-extras-openoffice

Source: %name-%version.tar

%description
Set of OpenOffice.org guides from Infra-Resource.

%files

%changelog
* Mon Apr 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- obsoletes old packages:
  + docs-openoffice-kirill
  + alt-docs-extras-openoffice

* Mon Apr 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

