Name: glances
Version: 2.11.1
Release: alt1
Summary: CLI curses based monitoring tool

Group: Monitoring
License: GPLv3
Url: https://github.com/nicolargo/glances
# Repacked %url/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Requires: python3-module-%name = %EVR

%add_python3_req_skip bernhard
%add_python3_req_skip bottle
%add_python3_req_skip cassandra
%add_python3_req_skip cassandra.cluster
%add_python3_req_skip cassandra.util
%add_python3_req_skip couchdb
%add_python3_req_skip couchdb.mapping
%add_python3_req_skip docker
%add_python3_req_skip elasticsearch
%add_python3_req_skip influxdb
%add_python3_req_skip influxdb.client
%add_python3_req_skip influxdb.influxdb08
%add_python3_req_skip influxdb.influxdb08.client
%add_python3_req_skip kafka
%add_python3_req_skip matplotlib
%add_python3_req_skip netifaces
%add_python3_req_skip nvidia-ml-py3
%add_python3_req_skip pika
%add_python3_req_skip potsdb
%add_python3_req_skip prometheus_client
%add_python3_req_skip py-cpuinfo
%add_python3_req_skip pymdstat
%add_python3_req_skip pysnmp
%add_python3_req_skip pystache
%add_python3_req_skip zmq
%add_python3_req_skip zmq.utils.strtypes
%add_python3_req_skip requests
%add_python3_req_skip scandir
%add_python3_req_skip statsd
%add_python3_req_skip wifi
%add_python3_req_skip zeroconf
%add_python_req_skip bernhard
%add_python_req_skip bottle
%add_python_req_skip cassandra
%add_python_req_skip couchdb
%add_python_req_skip docker
%add_python_req_skip elasticsearch
%add_python_req_skip influxdb
%add_python_req_skip kafka
%add_python_req_skip matplotlib
%add_python_req_skip netifaces
%add_python_req_skip nvidia-ml-py3
%add_python_req_skip pika
%add_python_req_skip potsdb
%add_python_req_skip prometheus_client
%add_python_req_skip py-cpuinfo
%add_python_req_skip pymdstat
%add_python_req_skip pysnmp
%add_python_req_skip pystache
%add_python_req_skip zmq
%add_python_req_skip requests
%add_python_req_skip scandir
%add_python_req_skip statsd
%add_python_req_skip wifi
%add_python_req_skip zeroconf

BuildRequires(pre): rpm-build-python3

BuildRequires: python-devel python-module-setuptools
BuildRequires: python3-devel python3-module-setuptools

%{?!_without_check:%{?!_disable_check:BuildRequires: /proc python-module-psutil python3-module-psutil}}

%description
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%package -n python-module-%name
Summary: CLI curses based monitoring tool
Group: Development/Python

%description -n python-module-%name
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%package -n python3-module-%name
Summary: CLI curses based monitoring tool
Group: Development/Python3

%description -n python3-module-%name
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%prep
%setup

%build
%python_build
%python3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%python_install
%python3_install

%check
python setup.py test
python3 setup.py test

%files -n python-module-%name
%doc AUTHORS COPYING README.rst NEWS
%python_sitelibdir/%name/
%python_sitelibdir/Glances-%version-py%_python_version.egg-info/
%exclude %_datadir/doc/glances

%files -n python3-module-%name
%doc AUTHORS COPYING README.rst NEWS
%python3_sitelibdir/%name/
%python3_sitelibdir/Glances-%version-py%_python3_version.egg-info/

%files
%_bindir/glances
%_man1dir/glances.1*

%changelog
* Wed Oct 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.11.1-alt1
- Initial build.
