%global import_path github.com/dalibo/ldap2pg
Name:    ldap2pg
Version: 6.5.1
Release: alt1

Summary: Manage PostgreSQL roles and privileges from YAML or LDAP
License: PostgreSQL
Group:   Other
Url:     https://github.com/dalibo/ldap2pg

Source0: %name-%version.tar
Source1: vendor.tar
Source2: ldap2pg.service 
Source3: ldap2pg.timer

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: systemd
Requires(pre): systemd

%description
%summary

%prep
%setup -q -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -D -m0644 ldap2pg.yml \
        %buildroot%_sysconfdir/ldap2pg/ldap2pg.yml

install -D -m0644 %SOURCE2 \
        %buildroot%_unitdir/ldap2pg.service

install -D -m0644 %SOURCE3 \
        %buildroot%_unitdir/ldap2pg.timer
%post 
%systemd_post ldap2pg.service ldap2pg.timer 

%preun 
%systemd_preun ldap2pg.service ldap2pg.timer 

%postun 
%systemd_postun_with_restart ldap2pg.service


%files
%doc README.md LICENSE

%_bindir/ldap2pg 

%config(noreplace) %_sysconfdir/ldap2pg/ldap2pg.yml 

%_unitdir/ldap2pg.service 
%_unitdir/ldap2pg.timer

%changelog
* Sat Jun 27 2026 Olesya Shuster <lesyafox@altlinux.org> 6.5.1-alt1
- Initial build for Sisyphus
