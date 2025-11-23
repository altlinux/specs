%define _unpackaged_files_terminate_build 1

Name: fonts-fork-awesome
Version: 1.2.0
Release: alt1

Summary: fork of the iconic font and CSS toolkit
License: CC-BY-3.0 AND OFL-1.1
Group: Other
Url: https://github.com/ForkAwesome/Fork-Awesome
Vcs: https://salsa.debian.org/fonts-team/fonts-fork-awesome

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ruby

BuildRequires: gem-fontcustom
BuildRequires: thor
BuildRequires: woff2
BuildRequires: python3(setuptools)

BuildArch: noarch

%description
Fork Awesome is a full suite of 718 pictographic icons for easy
scalable vector graphics on websites, originally created by
Dave Gandy and now maintained by a community.

%prep
%setup

%build
export FA_FONTCUSTOM_OUTPUT_DIR=src/icons/forkawesome
export FA_ROOT_FONTS_DIR=fonts

mkdir -p ${FA_ROOT_FONTS_DIR}

echo "Compiling Icons into a ForkAwesome fonts..."
pushd src/icons && \
                   fontcustom compile --debug
popd

echo "Copying builds to root folder (package release)..."
cp -v ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.eot ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.eot
cp -v ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.svg ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.svg
cp -v ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.ttf ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.ttf
cp -v ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.woff ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.woff
cp -v ${FA_FONTCUSTOM_OUTPUT_DIR}/forkawesome.woff2 ${FA_ROOT_FONTS_DIR}/forkawesome-webfont.woff2

%install
mkdir -pv %buildroot%_datadir/fonts-fork-awesome/fonts
mkdir -pv %buildroot%_datadir/javascript

mkdir -pv %buildroot%_datadir/fonts/ttf/fork-awesome/
cp -pv fonts/forkawesome-webfont.ttf %buildroot%_datadir/fonts/ttf/fork-awesome/

mkdir -pv %buildroot%_datadir/fonts/svg/fork-awesome/
cp -pv fonts/forkawesome-webfont.svg %buildroot%_datadir/fonts/svg/fork-awesome/

mkdir -pv %buildroot%_datadir/fonts/eot/fork-awesome/
cp -pv fonts/forkawesome-webfont.eot %buildroot%_datadir/fonts/eot/fork-awesome/

mkdir -pv %buildroot%_datadir/fonts/woff/fork-awesome/
cp -pv fonts/forkawesome-webfont.woff %buildroot%_datadir/fonts/woff/fork-awesome/

mkdir -pv %buildroot%_datadir/fonts/woff/fork-awesome/
cp -pv fonts/forkawesome-webfont.woff2 %buildroot%_datadir/fonts/woff/fork-awesome/

mkdir -pv %buildroot%_datadir/fonts-fork-awesome/
cp -arv less/ %buildroot%_datadir/fonts-fork-awesome/
cp -arv css/ %buildroot%_datadir/fonts-fork-awesome/
cp -arv scss/ %buildroot%_datadir/fonts-fork-awesome/

ln -srv %buildroot%_datadir/fonts/ttf/fork-awesome/forkawesome-webfont.ttf %buildroot%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.ttf
ln -srv %buildroot%_datadir/fonts/eot/fork-awesome/forkawesome-webfont.eot %buildroot%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.eot
ln -srv %buildroot%_datadir/fonts/svg/fork-awesome/forkawesome-webfont.svg %buildroot%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.svg
ln -srv %buildroot%_datadir/fonts/woff/fork-awesome/forkawesome-webfont.woff %buildroot%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.woff
ln -srv %buildroot%_datadir/fonts/woff/fork-awesome/forkawesome-webfont.woff2 %buildroot%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.woff2
ln -srv %buildroot%_datadir/fonts-fork-awesome %buildroot%_datadir/javascript/fork-awesome

cp -v src/icons/icons.yml  %buildroot%_datadir/fonts-fork-awesome/

%files
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md LICENSES README.md

%dir %_datadir/fonts-fork-awesome
%dir %_datadir/fonts-fork-awesome/css
%_datadir/fonts-fork-awesome/css/fork-awesome.css
%_datadir/fonts-fork-awesome/css/v5-compat.css
%dir %_datadir/fonts-fork-awesome/fonts
%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.eot
%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.svg
%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.ttf
%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.woff
%_datadir/fonts-fork-awesome/fonts/forkawesome-webfont.woff2
%_datadir/fonts-fork-awesome/icons.yml
%dir %_datadir/fonts-fork-awesome/less
%_datadir/fonts-fork-awesome/less/animated.less
%_datadir/fonts-fork-awesome/less/bordered-pulled.less
%_datadir/fonts-fork-awesome/less/core.less
%_datadir/fonts-fork-awesome/less/fixed-width.less
%_datadir/fonts-fork-awesome/less/fork-awesome.less
%_datadir/fonts-fork-awesome/less/icons.less
%_datadir/fonts-fork-awesome/less/larger.less
%_datadir/fonts-fork-awesome/less/list.less
%_datadir/fonts-fork-awesome/less/mixins.less
%_datadir/fonts-fork-awesome/less/path.less
%_datadir/fonts-fork-awesome/less/rotated-flipped.less
%_datadir/fonts-fork-awesome/less/screen-reader.less
%_datadir/fonts-fork-awesome/less/stacked.less
%_datadir/fonts-fork-awesome/less/v5-compat.less
%_datadir/fonts-fork-awesome/less/variables.less
%dir %_datadir/fonts-fork-awesome/scss
%_datadir/fonts-fork-awesome/scss/_animated.scss
%_datadir/fonts-fork-awesome/scss/_bordered-pulled.scss
%_datadir/fonts-fork-awesome/scss/_core.scss
%_datadir/fonts-fork-awesome/scss/_fixed-width.scss
%_datadir/fonts-fork-awesome/scss/_functions.scss
%_datadir/fonts-fork-awesome/scss/_icons.scss
%_datadir/fonts-fork-awesome/scss/_larger.scss
%_datadir/fonts-fork-awesome/scss/_list.scss
%_datadir/fonts-fork-awesome/scss/_mixins.scss
%_datadir/fonts-fork-awesome/scss/_path.scss
%_datadir/fonts-fork-awesome/scss/_rotated-flipped.scss
%_datadir/fonts-fork-awesome/scss/_screen-reader.scss
%_datadir/fonts-fork-awesome/scss/_stacked.scss
%_datadir/fonts-fork-awesome/scss/_variables.scss
%_datadir/fonts-fork-awesome/scss/fork-awesome.scss
%dir %_datadir/fonts/eot
%dir %_datadir/fonts/eot/fork-awesome
%_datadir/fonts/eot/fork-awesome/forkawesome-webfont.eot
%dir %_datadir/fonts/svg
%dir %_datadir/fonts/svg/fork-awesome
%_datadir/fonts/svg/fork-awesome/forkawesome-webfont.svg
%dir %_datadir/fonts/ttf
%dir %_datadir/fonts/ttf/fork-awesome
%_datadir/fonts/ttf/fork-awesome/forkawesome-webfont.ttf
%dir %_datadir/fonts/woff
%dir %_datadir/fonts/woff/fork-awesome
%_datadir/fonts/woff/fork-awesome/forkawesome-webfont.woff
%_datadir/fonts/woff/fork-awesome/forkawesome-webfont.woff2
%dir %_datadir/javascript/fork-awesome

%changelog
* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
