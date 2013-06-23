%define pkg nodejs
Name: rpm-build-%pkg
Version: 0.2
Release: alt1

Summary: RPM helper scripts for building %pkg packages

License: GPL
Group: Development/Other
URL: http://www.altlinux.org/Node.JS_Policy

Source: %name-%version.tar

BuildArch: noarch

%description
RPM helper scripts and build environment
for building %pkg packages.

See %url for detailed %pkg packaging policy.

%package -n rpm-macros-%pkg
Summary: RPM helper macros for building %pkg packages

License: GPL
Group: Development/Other

%description -n rpm-macros-%pkg
RPM marcos for building %pkg packages.

See %url for detailed %pkg packaging policy.

%prep
%setup

%install
mkdir -p %buildroot/%_rpmmacrosdir/
cat >> %buildroot/%_rpmmacrosdir/%pkg << 'EOF'
%%_rpm_build_nodejsdir	%%_datadir/%name
%%nodejs_arches	%%ix86 x86_64 %%arm
EOF
sed -e s,_rpmconfigdir,_rpm_build_nodejsdir,g macros.nodejs >> %buildroot/%_rpmmacrosdir/%pkg

install -D -m755 %pkg.prov %buildroot/usr/lib/rpm/%pkg.prov
install -D -m755 %pkg.prov.files %buildroot/usr/lib/rpm/%pkg.prov.files
install -D -m755 %pkg.req %buildroot/usr/lib/rpm/%pkg.req
ln -s %pkg.prov.files %buildroot/usr/lib/rpm/%pkg.req.files
install -D -m755 nodejs-fixdep  %buildroot%_datadir/%name/%pkg-fixdep
install -D -m755 nodejs-symlink-deps  %buildroot%_datadir/%name/%pkg-symlink-deps

%files
%_datadir/%name
/usr/lib/rpm/%pkg.prov
/usr/lib/rpm/%pkg.prov.files
/usr/lib/rpm/%pkg.req
/usr/lib/rpm/%pkg.req.files

%files -n rpm-macros-%pkg
%_rpmmacrosdir/%pkg

%changelog
* Sun Jun 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- bugfixes
- TODO: sync with nodejs-0.10.12-1 after node update

* Sat Jun 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
