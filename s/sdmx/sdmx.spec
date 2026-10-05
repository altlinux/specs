%define _destdir %_datadir/PolicyDefinitions
%define _schemadir %_datadir/xml/sdmx/1.0
%define _unpackaged_files_terminate_build 1

%def_with check
%def_with docs

Name: sdmx
Version: 1.0.0
Release: alt1

Summary: SDMX schemas, documentation and BaseALT policy templates
License: AGPL-3.0+
Group: System/Configuration/Other
Url: https://altlinux.space/alt-domain/sdmx-basealt
Vcs: https://altlinux.space/alt-domain/sdmx-basealt.git
BuildArch: noarch

%if_with check
BuildRequires: xml-utils
BuildRequires: python3
%endif

%if_with docs
BuildRequires: typst >= 0.13.1
BuildRequires: fonts-otf-mozilla-fira
BuildRequires: fonts-ttf-dejavu
BuildRequires: fonts-ttf-liberation
%endif

Source0: %name-%version.tar

%description
XML schemas and format documentation for SDMX/SDML, together with BaseALT
security policy templates and their localized resources.

%package -n sdmx-basealt
Summary: BaseALT SDMX policy templates
Group: System/Configuration/Other

%description -n sdmx-basealt
SDMX policy templates and localized SDML resources for managing security
settings through Group Policy tools on ALT operating systems.

%package -n sdmx-schemas
Summary: XML schemas for SDMX and SDML 1.0
Group: System/Configuration/Other

%description -n sdmx-schemas
Versioned SDMX/SDML 1.0 XML schemas and their local import dependencies.
The schemas can be used independently of the BaseALT policy templates.

%if_with docs
%package docs
Summary: SDMX and SDML format specification
Group: Documentation

%description docs
The normative SDMX/SDML 1.0 specification in PDF, including examples and
the XML schema appendices. Built from the bundled Typst sources offline.
%endif

%prep
%setup -q

%build
%if_with docs
# Do not depend on the builder's personal fonts or the wall-clock build time.
typst compile --root . --ignore-system-fonts \
    --font-path /usr/share/fonts/otf/mozilla-fira:/usr/share/fonts/ttf/dejavu:/usr/share/fonts/ttf/liberation \
    --creation-timestamp "${SOURCE_DATE_EPOCH:-$(stat -c %%Y docs/SDMX-SDML-1.0.typ)}" \
    docs/SDMX-SDML-1.0.typ docs/SDMX-SDML.pdf
%endif

%install
%__install -d -m0755 %buildroot%_destdir/{ru-RU,en-US}
%__install -pm0644 definitions/*.sdmx %buildroot%_destdir/
%__install -pm0644 definitions/ru-RU/*.sdml %buildroot%_destdir/ru-RU/
%__install -pm0644 definitions/en-US/*.sdml %buildroot%_destdir/en-US/
%__install -d -m0755 %buildroot%_schemadir/microsoft
%__install -pm0644 docs/schema/*.xsd %buildroot%_schemadir/
%__install -pm0644 docs/schema/microsoft/*.xsd %buildroot%_schemadir/microsoft/

%check
%if_with check
sh scripts/validate
%__python3 -m unittest discover -s tests
%__python3 scripts/check_package.py --root %buildroot
%endif
%if %{with check} && %{with docs}
%__python3 scripts/check_package.py --root %buildroot --pdf docs/SDMX-SDML.pdf
%endif

%files -n sdmx-basealt
%doc LICENSE Readme.md
%_destdir

%files -n sdmx-schemas
%doc LICENSE
%dir %_datadir/xml/sdmx
%_schemadir

%if_with docs
%files docs
%doc LICENSE Readme.md docs/SDMX-SDML.pdf
%endif

%changelog
* Thu Oct 01 2026 Korney Gedert <kiper@altlinux.org> 1.0.0-alt1
- Release SDMX/SDML 1.0
- Package versioned XML schemas and build the PDF documentation with Typst

Co-authored-by: Vladimir Rubanov <august@altlinux.org>

* Fri Sep 18 2026 Korney Gedert <kiper@altlinux.org> 0.1.0-alt1
- Initial release

Co-authored-by: Vladimir Rubanov <august@altlinux.org>
