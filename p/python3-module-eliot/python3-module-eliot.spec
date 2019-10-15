%define modulename eliot

Name: python3-module-eliot
Version: 1.10.0
Release: alt1

Summary: Logging library that tells you why it happened

Url: https://github.com/itamarst/eliot/
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/e/%modulename/%modulename-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
Python's built-in logging and other similar systems output a stream of factoids:
they're interesting, but you can't really tell what's going on.

* Why is your application slow?
* What caused this code path to be chosen?
* Why did this error happen?
* Standard logging can't answer these questions.

But with a better model you could understand what and why things happened in your application.
You could pinpoint performance bottlenecks, you could understand what happened when, who called what.

That is what Eliot does. eliot is a Python logging system that outputs causal chains of actions:
actions can spawn other actions, and eventually they either succeed or fail.
The resulting logs tell you the story of what your software did: what happened, and what caused it.

Eliot supports a range of use cases and 3rd party libraries:
* Logging within a single process.
* Causal tracing across a distributed system.
* Scientific computing, with built-in support for NumPy and Dask.
* Asyncio and Trio coroutines and the Twisted networking framework.

Eliot is only used to generate your logs; you will might need tools like Logstash and ElasticSearch
to aggregate and store logs if you are using multiple processes across multiple machines.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -rfv %buildroot%python3_sitelibdir/%modulename/dask.py*
rm -rfv %buildroot%python3_sitelibdir/%modulename/tests/

%files
%_bindir/eliot-prettyprint
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- initial build for ALT Sisyphus
