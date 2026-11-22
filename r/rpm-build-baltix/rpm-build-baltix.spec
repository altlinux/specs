Name:          rpm-build-baltix
Version:       0.2
Release:       alt1
Summary:       RPM dependency generators for Baltix
License:       MIT
Group:         Development/Ruby
BuildArch:     noarch
Url:           https://altlinux.space/majioa/baltix
Vcs:           https://altlinux.space/majioa/baltix.git
Packager:      Baltix Development Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
Requires:      rpm-macros-baltix = %EVR

%description
RPM dependency generators that read versioned requirements and capabilities
prepared by Baltix for each binary package.


%package       -n rpm-macros-baltix
Summary:       RPM macros for building with Baltix
Group:         Development/Ruby
BuildArch:     noarch
Requires:      ruby >= 3.0.0

%description   -n rpm-macros-baltix
RPM build actions and Ruby layout macros for Baltix.


%prep
%setup

%install
install -Dpm 0644 macros.baltix %buildroot%_rpmlibdir/macros.d/baltix
install -Dpm 0644 baltix.env %buildroot%_rpmlibdir/macros.d/baltix.env
install -Dpm 0755 baltix.deps %buildroot%_rpmlibdir/baltix.deps
install -Dpm 0755 baltix.req %buildroot%_rpmlibdir/baltix.req
install -Dpm 0755 baltix.req.files %buildroot%_rpmlibdir/baltix.req.files
install -Dpm 0755 baltix.prov %buildroot%_rpmlibdir/baltix.prov
install -Dpm 0755 baltix.prov.files %buildroot%_rpmlibdir/baltix.prov.files


%files
%doc LICENSE
%_rpmlibdir/macros.d/baltix.env
%_rpmlibdir/baltix.deps
%_rpmlibdir/baltix.req
%_rpmlibdir/baltix.req.files
%_rpmlibdir/baltix.prov
%_rpmlibdir/baltix.prov.files


%files         -n rpm-macros-baltix
%doc LICENSE
%_rpmlibdir/macros.d/baltix


%changelog
* Sun Nov 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.2-alt1
- + Added dependency generation on demand through Baltix predeps.
- * Updated RPM action macros and adopted the standard Ruby layout.
- * Retained the macros needed to rebuild gem-baltix 0.2-alt1.

* Thu Nov 19 2026 Pavel Skrylev <majioa@altlinux.org> 0.1-alt1
- + built rpm-build-baltix 0.1 for Sisyphus.
- + packaged the RPM build macros and dependency generators
