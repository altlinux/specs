Name:          rpm-build-baltix
Version:       0.1
Release:       alt1
Summary:       RPM dependency generators for Baltix
License:       Unlicense
Group:         Development/Ruby
BuildArch:     noarch
Url:           https://github.org/majioa/baltix
Vcs:           https://github.org/majioa/baltix.git

Source:        %name-%version.tar
Requires:      rpm-macros-baltix = %version-%release

%description
RPM dependency generators that read versioned requirements and capabilities
prepared by Baltix for each binary package.


%package       -n rpm-macros-baltix
Version:       0.1
Release:       alt1
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
install -Dpm 0755 baltix.req %buildroot%_rpmlibdir/baltix.req
install -Dpm 0755 baltix.req.files %buildroot%_rpmlibdir/baltix.req.files
install -Dpm 0755 baltix.prov %buildroot%_rpmlibdir/baltix.prov
install -Dpm 0755 baltix.prov.files %buildroot%_rpmlibdir/baltix.prov.files


%files
%_rpmlibdir/macros.d/baltix.env
%_rpmlibdir/baltix.req
%_rpmlibdir/baltix.req.files
%_rpmlibdir/baltix.prov
%_rpmlibdir/baltix.prov.files

%files         -n rpm-macros-baltix
%_rpmlibdir/macros.d/baltix


%changelog
* Thu Nov 19 2026 Pavel Skrylev <majioa@altlinux.org> 0.1-alt1
- + built rpm-build-baltix 0.1 for Sisyphus.
- + packaged the RPM build macros and dependency generators
