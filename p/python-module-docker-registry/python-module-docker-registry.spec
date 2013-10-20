%define oname docker-registry
Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Registry server for Docker (hosting/delivering of repositories and images)

Group: Development/Python
License: and ASL 2.0
Url: https://github.com/dotcloud/docker-registry
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: python-devel libevent-devel
Requires: python-module-gunicorn redis

%description
Registry server for Docker (hosting/delivering of repositories and images)

%prep
%setup

%build

%install
mkdir -p %buildroot%python_sitelibdir_noarch/%oname
cp -r lib %buildroot%python_sitelibdir_noarch/%oname/
cp -r registry %buildroot%python_sitelibdir_noarch/%oname/
cp -r scripts %buildroot%python_sitelibdir_noarch/%oname/
cp wsgi.py %buildroot%python_sitelibdir_noarch/%oname/

mkdir -p %buildroot%_sysconfdir/%oname
cp config_sample.yml config.yml
export SETTINGS_FLAVOR=prod
./setup-configs.sh
sed -i '/storage_path:/s/:.*/: \/var\/lib\/docker-registry/g' config.yml
cp config.yml %buildroot%_sysconfdir/%oname/config.yml
ln -s %_sysconfdir/%oname/config.yml %buildroot%python_sitelibdir_noarch/%oname/config.yml

mkdir -p %buildroot%_localstatedir/%oname

install -pD -m755 altlinux.init %buildroot%_initdir/%oname

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << EOF > %buildroot%_sysconfdir/sysconfig/%oname
LISTEN_IP="0.0.0.0"
LISTEN_PORT=5000
GUNICORN_WORKERS=2

EOF

%post
%post_service %oname

%preun
%preun_service %oname

%files
%doc README.* LICENSE
%python_sitelibdir_noarch/%oname
%_initdir/%oname
%config(noreplace) %_sysconfdir/sysconfig/%oname
%dir %_sysconfdir/%oname
%config(noreplace) %_sysconfdir/%oname/config.yml
%dir %_localstatedir/%oname

%changelog
* Sun Oct 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.1-alt1
- Build for ALT
