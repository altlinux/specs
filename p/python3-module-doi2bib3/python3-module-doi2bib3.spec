%define _unpackaged_files_terminate_build 1

%define pypi_name doi2bib3

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: DOI/arXiv to BibTeX command line utility
License: GPL-3.0-or-later
Group: Publishing
URL: https://github.com/archisman-panigrahi/doi2bib3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
doi2bib3 is a small Python utility to fetch BibTeX metadata for a DOI
or to resolve arXiv identifiers to DOIs and fetch their BibTeX entries.
It accepts DOI inputs, DOI URLs, arXiv IDs/URLs (modern and legacy),
publisher landing pages, and uses a sequence of resolution strategies
to return a BibTeX string.
This tool combines the features of doi2bib and doi2bib2.

Key behaviors

* Provides bibtex entry for DOI and arXiv links.
* Automatically detects arXiv inputs (e.g. 2411.08091, arXiv:2411.08091,
  or https://arxiv.org/abs/2411.08091) and queries the arXiv API for a DOI.
* For non-arXiv inputs: attempts DOI normalization, content negotiation at
  doi.org, Crossref transform, and as a last resort a Crossref bibliographic
  search.

A GUI frontend is available: Check out QuickBib.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS.md LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat May 23 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Thu May 21 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- New version 1.0.0.

* Fri May 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.3-alt1
- New version 0.5.3.

* Fri Dec 19 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.2-alt1
- New version 0.5.2.

* Sun Dec 07 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Fri Nov 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- new version 0.3.2 (with rpmrb script)

* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
