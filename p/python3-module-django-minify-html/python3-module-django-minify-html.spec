%define _unpackaged_files_terminate_build 1

%define oname django-minify-html

%def_with check

Name: python3-module-%oname
Version: 1.5.0
Release: alt1

Summary: Use minify-html, the extremely fast HTML + JS + CSS minifier, with Django.
License: MIT
Group: Development/Python3
Url: https://github.com/adamchainz/django-minify-html
ExcludeArch: i586 armh

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-minify-html

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_django)
BuildRequires: python3(pytest_randomly)
BuildRequires: python3-module-minify-html
BuildRequires: python3-module-django
BuildRequires: python3-module-coverage
BuildRequires: python3-module-django-tests
%endif

%description
HTML minification is an underappreciated techinque for web optimization.
It can yield significant savings, even on top of other tools like
compression with Brotli or Gzip.

There are other minifiers out there, but in benchmarks minify-html
surpasses them all. It's a really well optimized and tested Rust library,
and seems to be the best available HTML minifier.

Some CDN's provide automatic minification, such as CloudFlare. This can be
convenient, since it requires no application changes. But it adds some
overhead: non-minified HTML has to first be transferred to the CDN, and
the CDN has to parse the response, and recombine it. It also means that
you don't get to see the potential side effects of minification until your
code is live. Overall it should be faster and more predictable to minify
within Django, at the point of HTML generation.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
        %buildroot%python3_sitelibdir/
%endif

%check
%tox_check_pyproject

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Wed Apr 19 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 1.5.0-alt1
- New version 1.5.0
  + migrate to pyproject

* Tue Sep 20 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 1.3.0-alt1
- New version 1.3.0
  + Move .spec in the "alt" directory

* Fri Feb 18 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux
