%define oname SimPy
Name: python-module-%oname
Version: 1.8
Release: alt2.1

Summary: SimPy simulation package

License: LGPL
Group: Development/Python
Url: http://simpy.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://ftputil.sschwarzer.net/trac/attachment/wiki/Download/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# Automatically added by buildreq on Sun Oct 28 2007
BuildRequires: python-devel python-modules-compiler

%description
SimPy is a process-based discrete-event simulation language
based on standard Python and released under the GNU LGPL.

It provides the modeller with components of a simulation
model. These include processes, for active components like
customers, messages, and vehicles, and resources, for
passive components that form limited capacity congestion
points like servers, checkout counters, and tunnels. It
also provides monitor variables to aid in gathering
statistics. SimPy comes with extensive plotting capabilities.

The distribution contains in-depth documentation, tutorials,
and a large number of simulation models.

Simulation model developers are encouraged to share their
SimPy modeling techniques with the SimPy community. Please
post a message to the simpy-Users mailing list,


%prep
%setup -q -n %oname-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

%files
%doc SimPyDocs SimPyModels
%doc CHANGES_FROM_PREVIOUS_VERSION.* COMPATIBILITY.* HISTORY.* README.*
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.8-alt1.1
- Rebuilt with python-2.5.

* Sun Oct 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- initial build for ALT Linux Sisyphus
