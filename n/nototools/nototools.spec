%filter_from_requires /^python2.7(font_caching)/d
%filter_from_requires /^python2.7(render)/d
%filter_from_requires /^python2.7(booleanOperations)/d
%filter_from_requires /^python2.7(defcon)/d
%filter_from_requires /^python2.7(ufoLib)/d
Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: gcc-c++ python-module-setuptools python3-module-setuptools
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit0 0c99dfff2a824c6f7210ff700c56b2c3d51e64cd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# can't compile with python 3.x
%define python3 %{nil}

%global common_desc \
The nototools python package contains python scripts \
used to maintain the Noto Fonts project, \
including the google.com/get/noto website.

Name:		nototools
Version:	0
Release:	alt1_0.20170929.git%{shortcommit0}
Summary:	Noto fonts support tools and scripts plus web site generation

# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
License:	ASL 2.0
URL:		https://github.com/googlei18n/nototools
Source0:	https://github.com/googlei18n/nototools/archive/%{commit0}.tar.gz#/nototools-%{shortcommit0}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
%if %{with python3}
BuildRequires:	python3-devel
%endif # with python3

Requires:	python-module-nototools = %{version}-%{release}
Source44: import.info

%description
%common_desc

%if %{with python3}
%package     -n python3-module-nototools
Group: Other
Summary:	Noto tools for python 3

%description -n python3-module-nototools
%common_desc

%endif # with python3

%package     -n python-module-nototools
Group: Other
Summary:	Noto tools for python 2
Requires:	python-module-fonttools
BuildRequires:	python-module-fonttools

%description -n python-module-nototools
%common_desc

%prep
%setup -q -c

# remove unneeded files
rm -rf nototools-%{commit0}/third_party/{cldr,dspl,fontcrunch,ohchr,spiro,udhr,unicode}
mv %{name}-%{commit0} python2

%if %{with python3}
cp -a python2 python3
%endif # with python3

# for documents
cp python2/*.md python2/LICENSE .

%build
pushd python2
%python_build
popd

%if %{with python3}
pushd python3
%python3_build
popd
%endif # with python3


%install
%if %{with python3}
pushd python3
%python3_install
popd
%endif # with python3

pushd python2
%python_install
for lib in %{buildroot}%{python_sitelibdir_noarch}/nototools/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
popd


%check
pushd python2
%{__python} setup.py test
popd

%if %{with python3}
pushd python3
%{__python3} setup.py test
popd
%endif


%files
%doc --no-dereference LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/add_vs_cmap.py
%{_bindir}/autofix_for_release.py
%{_bindir}/create_image.py
%{_bindir}/decompose_ttc.py
%{_bindir}/drop_hints.py
%{_bindir}/dump_otl.py
%{_bindir}/fix_khmer_and_lao_coverage.py
%{_bindir}/fix_noto_cjk_thin.py
%{_bindir}/generate_sample_text.py
%{_bindir}/generate_website_2_data.py
%{_bindir}/merge_fonts.py
%{_bindir}/merge_noto.py
%{_bindir}/noto_lint.py
%{_bindir}/notocoverage
%{_bindir}/notodiff
%{_bindir}/scale.py
%{_bindir}/subset.py
%{_bindir}/subset_symbols.py
%{_bindir}/test_vertical_extents.py


%files -n python-module-nototools
%{python_sitelibdir_noarch}/nototools
%{python_sitelibdir_noarch}/nototools-0.0.1-py2.7.egg-info
%{python_sitelibdir_noarch}/third_party

%if %{with python3}
%files -n python3-module-nototools
%{python3_sitelibdir_noarch}/nototools
%{python3_sitelibdir_noarch}/nototools-0.0.1-py3.?.egg-info
%{python3_sitelibdir_noarch}/third_party
%endif # with python3


%changelog
* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.20170929.git0c99dff
- new version

