
%define modname apiron
Name: python3-module-%modname
Version: 5.1.0
Release: alt1
Summary: Apiron helps you cook a tasty client for RESTful APIs
License: MIT
Group: Development/Python3
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: https://github.com/ithaka/apiron
Source: https://files.pythonhosted.org/packages/source/a/apiron/%modname-%version.tar.gz

BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build python3-module-urllib3 python3-module-yieldfrom.urllib3
BuildRequires:  python3-module-requests >= 2.11.1
Requires:       python3-module-requests >= 2.11.1
BuildArch: noarch
%add_python3_req_skip requests.packages.urllib3.util


%description
Gathering data from multiple services has become a ubiquitous task for web application developers. The complexity can grow quickly: calling an API endpoint with multiple parameter sets, calling multiple API endpoints, calling multiple endpoints in multiple APIs. While the business logic can get hairy, the code to interact with those APIs doesn't have to.

apiron provides declarative, structured configuration of services and endpoints with a unified interface for interacting with them.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files 
%doc README.md
%python3_sitelibdir/%modname/
%python3_sitelibdir/%modname-%version-py?.??.egg-info/

%changelog
* Fri May 06 2022 Ilya Mashkin <oddity@altlinux.ru> 5.1.0-alt1
- Build for Sisyphus

* Mon Aug 31 2020 Steve Kowalik <steven.kowalik@suse.com>
- Update to 5.1.0:
  * Ability to specify proxies for a Service definition so all calls to the
    service use the defined proxies
  * Ability to specify auth for a Service definition so all calls to the
    service use the defined authentication
  * Ability to specify return_raw_response_object at the endpoint level,
    overridden by any value specified at call time
* Tue Dec  3 2019 Tomáš Chvátal <tchvatal@suse.com>
- Drop needless service, one can call the command directly:
  osc service localrun download_files
- Fix the test call to really execute the tests
- Run the spec-cleaner
* Mon Dec  2 2019 Axel Braun <axel.braun@gmx.de>
- version 5.0.0
  tests added
* Mon Aug 26 2019 Axel Braun <axel.braun@gmx.de>
- version 4.1.0
  initial build on OBS
