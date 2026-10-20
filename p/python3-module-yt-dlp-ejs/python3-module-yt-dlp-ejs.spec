%define pypi_name yt-dlp-ejs
%define mod_name yt_dlp_ejs

Name: python3-module-yt-dlp-ejs
Version: 0.8.0
Release: alt1

Summary: External JavaScript for yt-dlp supporting many runtimes

# yt-dlp-ejs: Unlicense, bundled astring: MIT, bundled meriyah: ISC
License: Unlicense AND MIT AND ISC
Group: Development/Python3
Url: https://github.com/yt-dlp/ejs

# Source-url: https://github.com/yt-dlp/ejs/archive/%version.tar.gz
Source: %name-%version.tar
# node_modules with the JavaScript build dependencies (see .gear/predownloaded-preinstall-hook)
Source1: %name-development-%version.tar

BuildArch: noarch
# the system rollup is not built for i586
ExcludeArch: %ix86

BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-hatch-vcs
BuildRequires: rollup node /proc

%description
yt-dlp-ejs contains the JavaScript challenge solver scripts used by
yt-dlp to extract YouTube formats. The scripts are run by an external
JavaScript runtime (deno, node, bun or quickjs).

%prep
%setup -a1
# use the system rollup (built from source) instead of the npm one
ln -s %_prefix/lib/node_modules/rollup node_modules/rollup
# the bundles are built below, don't run npm/pnpm/deno from the hatch build hook
sed -i '/^\[tool\.hatch\.build\.targets\.wheel\.hooks\.custom\]/d' pyproject.toml

%build
rollup -c
# the bundles yt-dlp loads from the python package (see hatch_build.py)
cp -v dist/yt.solver.core.min.js %mod_name/yt/solver/core.min.js
cp -v dist/yt.solver.lib.min.js %mod_name/yt/solver/lib.min.js
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
# yt-dlp accepts only the bundles with the upstream release hashes
# (VERSION/HASHES in yt_dlp/extractor/youtube/jsc/_builtin/vendor/_info.py)
echo 'ee5b307d07f55e91e4723edf5ac205cc877a474187849d757dc1322e38427b157a9d706d510c1723d3670f98e5a3f8cbcde77874a80406bd7204bc9fea30f283 dist/yt.solver.core.min.js' > sha3.sum
echo '8420c259ad16e99ce004e4651ac1bcabb53b4457bf5668a97a9359be9a998a789fee8ab124ee17f91a2ea8fd84e0f2b2fc8eabcaf0b16a186ba734cf422ad053 dist/yt.solver.lib.min.js' >> sha3.sum
%__python3 -c 'import hashlib, sys
for line in open("sha3.sum"):
    digest, name = line.split()
    got = hashlib.sha3_512(open(name, "rb").read()).hexdigest()
    assert got == digest, f"{name} differs from the upstream release: {got}"
'
%__python3 -c 'import sys; sys.path.insert(0, "%buildroot%python3_sitelibdir"); import yt_dlp_ejs, yt_dlp_ejs.yt.solver as s; assert yt_dlp_ejs.version == "%version"; assert len(s.core()) > 1000 and len(s.lib()) > 1000'

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- initial build for Sisyphus
