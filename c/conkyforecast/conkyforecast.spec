Name:		conkyforecast
Version:	2.04
Release:	alt1.1.1
Summary:	Provides weather forecast information to be dislayed in conky.
Summary(ru_RU.UTF8): Скрипт Python для Conky для получения данных о погоде
Group:		Monitoring
License:	GPLv3
Packager:       Denis Koryavov <dkoryavov@altlinux.org>
URL:		https://code.launchpad.net/~m-buck/+junk/conkyforecast
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	python-module-setuptools
Requires:	conky

%description
conkyForecast is a python script created to provide weather forecast information
to be displayed in Conky. It uses the Weather.com XOAP service to retrieve data
for all over the world.

%description -l ru_RU.UTF8
Данный пакет содержит в себе исполняемый файл на языке Python предназначенный
отображения данных о погоде в системном мониторе Conky. Для получения данных
о погоде используется информация с сайта Weather.com.


%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %buildroot

%files
%doc AUTHORS COPYING CHANGELOG README
%{python_sitelibdir}/%name-%version-py*.egg-info 
%{_bindir}/conkyForecast
%{_datadir}/%name
%{_datadir}/fonts/truetype/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.04-alt1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.04-alt1.1
- Rebuilt with python 2.6

* Mon Aug 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 2.04-alt1
- First build for Sisyphus.


