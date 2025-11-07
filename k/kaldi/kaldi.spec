#
# Use script .gear/Update.sh to pass values to specsubst
# More information about specsubst:
# https://www.altlinux.org/Gear/specsubst
#

# See .gear/Update.sh
%global soversion 5
# See .gear/Update.sh
%global patch_number 1182

%global descr Kaldi is a toolkit for speech recognition written in C++ and licensed under the\
Apache License v2.0. Kaldi is intended for use by speech recognition\
researchers.

Name: kaldi
# See src/.version
Version: 5.5
Release: alt1.gite02e35f

Summary: Kaldi is a toolkit for speech recognition
License: Apache-2.0
Group: System/Libraries
Url: https://kaldi-asr.org
Vcs: https://github.com/kaldi-asr/kaldi.git

Source: %name-%version.tar
Patch: fix-kaldi-gite02e35f-ALT-cmake.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel
BuildRequires: libopenfst-devel
BuildRequires: ninja-build

# Build requires libopenfst-devel failed to build on the i586
ExcludeArch: %ix86

%description
%descr

%package -n libkaldi%soversion
Summary: Kaldi is a toolkit for speech recognition
Group: System/Libraries

%description -n libkaldi%soversion
%descr

%package -n libkaldi-devel
Summary: Development files for the %name
Group: Development/C++
Requires: libkaldi%soversion = %EVR

%description -n libkaldi-devel
%summary.
%descr

%package tools
Summary: Tools for the %name
Group: Other
Requires: libkaldi%soversion = %EVR

%description tools
%summary.
%descr

%prep
%setup
%autopatch
sed -i -e 's/@VERSION@/%version/g' \
	-e 's/@PATCH_NUMBER@/%patch_number/g' \
		cmake/VersionHelper.cmake

%build
%cmake -Wno-dev \
	-GNinja \
	-DFETCHCONTENT_FULLY_DISCONNECTED=ON \
	-DBuildForFedora=ON \
	-DBUILD_SHARED_LIBS=ON \
	-DKALDI_BUILD_TEST=OF \
	-DKALDI_USE_PATCH_NUMBER=ON
pushd %_cmake__builddir
%ninja_build
popd

%install
pushd %_cmake__builddir
%ninja_install
popd

%files -n libkaldi%soversion
%_libdir/libkaldi*.so.%{soversion}*

%files -n libkaldi-devel
%_includedir/%name
%_libdir/cmake/%name
%_libdir/libkaldi*.so

%files tools
%_bindir/acc-lda
%_bindir/acc-tree-stats
%_bindir/add-deltas
%_bindir/add-deltas-sdc
%_bindir/add-self-loops
%_bindir/agglomerative-cluster
%_bindir/ali-to-pdf
%_bindir/ali-to-phones
%_bindir/ali-to-post
%_bindir/align-compiled-mapped
%_bindir/align-equal
%_bindir/align-equal-compiled
%_bindir/align-mapped
%_bindir/align-text
%_bindir/am-info
%_bindir/analyze-counts
%_bindir/append-post-to-feats
%_bindir/append-vector-to-feats
%_bindir/apply-cmvn
%_bindir/apply-cmvn-online
%_bindir/apply-cmvn-sliding
%_bindir/arpa-to-const-arpa
%_bindir/arpa2fst
%_bindir/build-pfile-from-ali
%_bindir/build-tree
%_bindir/build-tree-two-level
%_bindir/chain-est-phone-lm
%_bindir/chain-get-supervision
%_bindir/chain-make-den-fst
%_bindir/chain-make-num-fst-e2e
%_bindir/cluster-phones
%_bindir/cmvn-to-nnet
%_bindir/compare-feats
%_bindir/compare-int-vector
%_bindir/compile-graph
%_bindir/compile-questions
%_bindir/compile-train-graphs
%_bindir/compile-train-graphs-fsts
%_bindir/compile-train-graphs-without-lexicon
%_bindir/compose-transforms
%_bindir/compress-uncompress-speex
%_bindir/compute-and-process-kaldi-pitch-feats
%_bindir/compute-atwv
%_bindir/compute-cmvn-stats
%_bindir/compute-cmvn-stats-two-channel
%_bindir/compute-eer
%_bindir/compute-fbank-feats
%_bindir/compute-gop
%_bindir/compute-kaldi-pitch-feats
%_bindir/compute-mfcc-feats
%_bindir/compute-plp-feats
%_bindir/compute-spectrogram-feats
%_bindir/compute-vad
%_bindir/compute-vad-from-frame-likes
%_bindir/compute-wer
%_bindir/compute-wer-bootci
%_bindir/concat-feats
%_bindir/convert-ali
%_bindir/copy-feats
%_bindir/copy-feats-to-htk
%_bindir/copy-feats-to-sphinx
%_bindir/copy-gselect
%_bindir/copy-int-vector
%_bindir/copy-matrix
%_bindir/copy-post
%_bindir/copy-transition-model
%_bindir/copy-tree
%_bindir/copy-vector
%_bindir/cuda-compiled
%_bindir/cuda-gpu-available
%_bindir/decode-faster
%_bindir/decode-faster-mapped
%_bindir/draw-tree
%_bindir/est-lda
%_bindir/est-mllt
%_bindir/est-pca
%_bindir/extend-transform-dim
%_bindir/extend-wav-with-silence
%_bindir/extract-feature-segments
%_bindir/extract-segments
%_bindir/feat-to-dim
%_bindir/feat-to-len
%_bindir/feat-to-post
%_bindir/fmpe-acc-stats
%_bindir/fmpe-apply-transform
%_bindir/fmpe-est
%_bindir/fmpe-init
%_bindir/fmpe-sum-accs
%_bindir/fstaddselfloops
%_bindir/fstaddsubsequentialloop
%_bindir/fstcomposecontext
%_bindir/fstcopy
%_bindir/fstdeterminizelog
%_bindir/fstdeterminizestar
%_bindir/fstisstochastic
%_bindir/fstmakecontextfst
%_bindir/fstmakecontextsyms
%_bindir/fstminimizeencoded
%_bindir/fstphicompose
%_bindir/fstpushspecial
%_bindir/fstrand
%_bindir/fstrmepslocal
%_bindir/fstrmsymbols
%_bindir/fsts-concat
%_bindir/fsts-project
%_bindir/fsts-to-transcripts
%_bindir/fsts-union
%_bindir/fsttablecompose
%_bindir/generate-proxy-keywords
%_bindir/get-full-lda-mat
%_bindir/get-post-on-ali
%_bindir/gmm-acc-mllt
%_bindir/gmm-acc-mllt-global
%_bindir/gmm-acc-stats
%_bindir/gmm-acc-stats-ali
%_bindir/gmm-acc-stats-twofeats
%_bindir/gmm-acc-stats2
%_bindir/gmm-adapt-map
%_bindir/gmm-align
%_bindir/gmm-align-compiled
%_bindir/gmm-basis-fmllr-accs
%_bindir/gmm-basis-fmllr-accs-gpost
%_bindir/gmm-basis-fmllr-training
%_bindir/gmm-boost-silence
%_bindir/gmm-compute-likes
%_bindir/gmm-copy
%_bindir/gmm-decode-biglm-faster
%_bindir/gmm-decode-faster
%_bindir/gmm-decode-faster-regtree-fmllr
%_bindir/gmm-decode-faster-regtree-mllr
%_bindir/gmm-decode-simple
%_bindir/gmm-est
%_bindir/gmm-est-basis-fmllr
%_bindir/gmm-est-basis-fmllr-gpost
%_bindir/gmm-est-fmllr
%_bindir/gmm-est-fmllr-global
%_bindir/gmm-est-fmllr-gpost
%_bindir/gmm-est-fmllr-raw
%_bindir/gmm-est-fmllr-raw-gpost
%_bindir/gmm-est-gaussians-ebw
%_bindir/gmm-est-lvtln-trans
%_bindir/gmm-est-map
%_bindir/gmm-est-regtree-fmllr
%_bindir/gmm-est-regtree-fmllr-ali
%_bindir/gmm-est-regtree-mllr
%_bindir/gmm-est-rescale
%_bindir/gmm-est-weights-ebw
%_bindir/gmm-fmpe-acc-stats
%_bindir/gmm-get-stats-deriv
%_bindir/gmm-global-acc-stats
%_bindir/gmm-global-acc-stats-twofeats
%_bindir/gmm-global-copy
%_bindir/gmm-global-est
%_bindir/gmm-global-est-fmllr
%_bindir/gmm-global-est-lvtln-trans
%_bindir/gmm-global-get-frame-likes
%_bindir/gmm-global-get-post
%_bindir/gmm-global-gselect-to-post
%_bindir/gmm-global-info
%_bindir/gmm-global-init-from-feats
%_bindir/gmm-global-sum-accs
%_bindir/gmm-global-to-fgmm
%_bindir/gmm-gselect
%_bindir/gmm-info
%_bindir/gmm-init-biphone
%_bindir/gmm-init-lvtln
%_bindir/gmm-init-model
%_bindir/gmm-init-model-flat
%_bindir/gmm-init-mono
%_bindir/gmm-ismooth-stats
%_bindir/gmm-latgen-biglm-faster
%_bindir/gmm-latgen-faster
%_bindir/gmm-latgen-faster-parallel
%_bindir/gmm-latgen-faster-regtree-fmllr
%_bindir/gmm-latgen-map
%_bindir/gmm-latgen-simple
%_bindir/gmm-make-regtree
%_bindir/gmm-mixup
%_bindir/gmm-post-to-gpost
%_bindir/gmm-rescore-lattice
%_bindir/gmm-sum-accs
%_bindir/gmm-train-lvtln-special
%_bindir/gmm-transform-means
%_bindir/gmm-transform-means-global
%_bindir/hmm-info
%_bindir/interpolate-pitch
%_bindir/ivector-adapt-plda
%_bindir/ivector-compute-dot-products
%_bindir/ivector-compute-lda
%_bindir/ivector-compute-plda
%_bindir/ivector-copy-plda
%_bindir/ivector-extract
%_bindir/ivector-extract-online
%_bindir/ivector-extract-online2
%_bindir/ivector-extractor-acc-stats
%_bindir/ivector-extractor-copy
%_bindir/ivector-extractor-est
%_bindir/ivector-extractor-init
%_bindir/ivector-extractor-sum-accs
%_bindir/ivector-mean
%_bindir/ivector-normalize-length
%_bindir/ivector-plda-scoring
%_bindir/ivector-plda-scoring-dense
%_bindir/ivector-randomize
%_bindir/ivector-subtract-global-mean
%_bindir/ivector-transform
%_bindir/kws-index-union
%_bindir/kws-search
%_bindir/latgen-faster-mapped
%_bindir/latgen-faster-mapped-parallel
%_bindir/latgen-incremental-mapped
%_bindir/lattice-1best
%_bindir/lattice-add-nnlmscore
%_bindir/lattice-add-penalty
%_bindir/lattice-add-trans-probs
%_bindir/lattice-align-phones
%_bindir/lattice-align-words
%_bindir/lattice-align-words-lexicon
%_bindir/lattice-arc-post
%_bindir/lattice-best-path
%_bindir/lattice-boost-ali
%_bindir/lattice-combine
%_bindir/lattice-compose
%_bindir/lattice-confidence
%_bindir/lattice-copy
%_bindir/lattice-copy-backoff
%_bindir/lattice-depth
%_bindir/lattice-depth-per-frame
%_bindir/lattice-determinize
%_bindir/lattice-determinize-non-compact
%_bindir/lattice-determinize-phone-pruned
%_bindir/lattice-determinize-phone-pruned-parallel
%_bindir/lattice-determinize-pruned
%_bindir/lattice-determinize-pruned-parallel
%_bindir/lattice-difference
%_bindir/lattice-equivalent
%_bindir/lattice-expand
%_bindir/lattice-expand-ngram
%_bindir/lattice-interp
%_bindir/lattice-limit-depth
%_bindir/lattice-lmrescore
%_bindir/lattice-lmrescore-const-arpa
%_bindir/lattice-lmrescore-kaldi-rnnlm
%_bindir/lattice-lmrescore-kaldi-rnnlm-pruned
%_bindir/lattice-lmrescore-pruned
%_bindir/lattice-lmrescore-rnnlm
%_bindir/lattice-mbr-decode
%_bindir/lattice-minimize
%_bindir/lattice-oracle
%_bindir/lattice-path-cover
%_bindir/lattice-project
%_bindir/lattice-prune
%_bindir/lattice-push
%_bindir/lattice-rescore-mapped
%_bindir/lattice-reverse
%_bindir/lattice-rmali
%_bindir/lattice-scale
%_bindir/lattice-to-ctm-conf
%_bindir/lattice-to-fst
%_bindir/lattice-to-kws-index
%_bindir/lattice-to-mpe-post
%_bindir/lattice-to-nbest
%_bindir/lattice-to-phone-lattice
%_bindir/lattice-to-post
%_bindir/lattice-to-smbr-post
%_bindir/lattice-union
%_bindir/linear-to-nbest
%_bindir/logistic-regression-copy
%_bindir/logistic-regression-eval
%_bindir/logistic-regression-train
%_bindir/logprob-to-post
%_bindir/make-grammar-fst
%_bindir/make-h-transducer
%_bindir/make-ilabel-transducer
%_bindir/make-pdf-to-tid-transducer
%_bindir/matrix-dim
%_bindir/matrix-max
%_bindir/matrix-sum
%_bindir/matrix-sum-rows
%_bindir/merge-vads
%_bindir/modify-cmvn-stats
%_bindir/multiply-vectors
%_bindir/nbest-to-ctm
%_bindir/nbest-to-lattice
%_bindir/nbest-to-linear
%_bindir/nbest-to-prons
%_bindir/nnet-adjust-priors
%_bindir/nnet-align-compiled
%_bindir/nnet-am-average
%_bindir/nnet-am-compute
%_bindir/nnet-am-copy
%_bindir/nnet-am-fix
%_bindir/nnet-am-info
%_bindir/nnet-am-init
%_bindir/nnet-am-mixup
%_bindir/nnet-am-reinitialize
%_bindir/nnet-am-switch-preconditioning
%_bindir/nnet-am-widen
%_bindir/nnet-combine
%_bindir/nnet-combine-egs-discriminative
%_bindir/nnet-combine-fast
%_bindir/nnet-compare-hash-discriminative
%_bindir/nnet-compute
%_bindir/nnet-compute-from-egs
%_bindir/nnet-compute-prob
%_bindir/nnet-concat
%_bindir/nnet-copy
%_bindir/nnet-copy-egs
%_bindir/nnet-copy-egs-discriminative
%_bindir/nnet-forward
%_bindir/nnet-get-egs
%_bindir/nnet-get-egs-discriminative
%_bindir/nnet-get-feature-transform
%_bindir/nnet-get-feature-transform-multi
%_bindir/nnet-get-weighted-egs
%_bindir/nnet-info
%_bindir/nnet-init
%_bindir/nnet-initialize
%_bindir/nnet-insert
%_bindir/nnet-latgen-faster
%_bindir/nnet-latgen-faster-parallel
%_bindir/nnet-modify-learning-rates
%_bindir/nnet-normalize-stddev
%_bindir/nnet-relabel-egs
%_bindir/nnet-replace-last-layers
%_bindir/nnet-set-learnrate
%_bindir/nnet-show-progress
%_bindir/nnet-shuffle-egs
%_bindir/nnet-shuffle-egs-discriminative
%_bindir/nnet-subset-egs
%_bindir/nnet-to-raw-nnet
%_bindir/nnet-train-discriminative-parallel
%_bindir/nnet-train-discriminative-simple
%_bindir/nnet-train-ensemble
%_bindir/nnet-train-frmshuff
%_bindir/nnet-train-mmi-sequential
%_bindir/nnet-train-mpe-sequential
%_bindir/nnet-train-multistream
%_bindir/nnet-train-multistream-perutt
%_bindir/nnet-train-parallel
%_bindir/nnet-train-perutt
%_bindir/nnet-train-simple
%_bindir/nnet-train-transitions
%_bindir/nnet1-to-raw-nnet
%_bindir/nnet3-acc-lda-stats
%_bindir/nnet3-align-compiled
%_bindir/nnet3-am-adjust-priors
%_bindir/nnet3-am-copy
%_bindir/nnet3-am-info
%_bindir/nnet3-am-init
%_bindir/nnet3-am-train-transitions
%_bindir/nnet3-average
%_bindir/nnet3-chain-acc-lda-stats
%_bindir/nnet3-chain-add-post-to-egs
%_bindir/nnet3-chain-combine
%_bindir/nnet3-chain-combine2
%_bindir/nnet3-chain-compute-post
%_bindir/nnet3-chain-compute-prob
%_bindir/nnet3-chain-copy-egs
%_bindir/nnet3-chain-e2e-get-egs
%_bindir/nnet3-chain-get-egs
%_bindir/nnet3-chain-merge-egs
%_bindir/nnet3-chain-normalize-egs
%_bindir/nnet3-chain-shuffle-egs
%_bindir/nnet3-chain-subset-egs
%_bindir/nnet3-chain-train
%_bindir/nnet3-chain-train2
%_bindir/nnet3-combine
%_bindir/nnet3-compute
%_bindir/nnet3-compute-batch
%_bindir/nnet3-compute-from-egs
%_bindir/nnet3-compute-prob
%_bindir/nnet3-copy
%_bindir/nnet3-copy-egs
%_bindir/nnet3-discriminative-compute-from-egs
%_bindir/nnet3-discriminative-compute-objf
%_bindir/nnet3-discriminative-copy-egs
%_bindir/nnet3-discriminative-get-egs
%_bindir/nnet3-discriminative-merge-egs
%_bindir/nnet3-discriminative-shuffle-egs
%_bindir/nnet3-discriminative-subset-egs
%_bindir/nnet3-discriminative-train
%_bindir/nnet3-egs-augment-image
%_bindir/nnet3-get-egs
%_bindir/nnet3-get-egs-dense-targets
%_bindir/nnet3-get-egs-simple
%_bindir/nnet3-info
%_bindir/nnet3-init
%_bindir/nnet3-latgen-faster
%_bindir/nnet3-latgen-faster-batch
%_bindir/nnet3-latgen-faster-lookahead
%_bindir/nnet3-latgen-faster-looped
%_bindir/nnet3-latgen-faster-looped-parallel
%_bindir/nnet3-latgen-faster-parallel
%_bindir/nnet3-latgen-grammar
%_bindir/nnet3-merge-egs
%_bindir/nnet3-show-progress
%_bindir/nnet3-shuffle-egs
%_bindir/nnet3-subset-egs
%_bindir/nnet3-train
%_bindir/nnet3-xvector-compute
%_bindir/nnet3-xvector-compute-batched
%_bindir/nnet3-xvector-get-egs
%_bindir/online-audio-client
%_bindir/online-audio-server-decode-faster
%_bindir/online-gmm-decode-faster
%_bindir/online-net-client
%_bindir/online-server-gmm-decode-faster
%_bindir/online-wav-gmm-decode-faster
%_bindir/online2-tcp-nnet3-decode-faster
%_bindir/online2-tcp-nnet3-decode-faster-emscripten
%_bindir/online2-wav-dump-features
%_bindir/online2-wav-gmm-latgen-faster
%_bindir/online2-wav-nnet2-am-compute
%_bindir/online2-wav-nnet2-latgen-faster
%_bindir/online2-wav-nnet2-latgen-threaded
%_bindir/online2-wav-nnet3-latgen-faster
%_bindir/online2-wav-nnet3-latgen-grammar
%_bindir/online2-wav-nnet3-latgen-incremental
%_bindir/online2-wav-nnet3-wake-word-decoder-faster
%_bindir/paste-feats
%_bindir/paste-post
%_bindir/paste-vectors
%_bindir/phones-to-prons
%_bindir/post-to-feats
%_bindir/post-to-pdf-post
%_bindir/post-to-phone-post
%_bindir/post-to-smat
%_bindir/post-to-tacc
%_bindir/post-to-weights
%_bindir/print-proxy-keywords
%_bindir/prob-to-post
%_bindir/process-kaldi-pitch-feats
%_bindir/process-pitch-feats
%_bindir/prons-to-wordali
%_bindir/raw-nnet-concat
%_bindir/raw-nnet-copy
%_bindir/raw-nnet-info
%_bindir/rbm-convert-to-nnet
%_bindir/rbm-train-cd1-frmshuff
%_bindir/rnnlm-compute-prob
%_bindir/rnnlm-get-egs
%_bindir/rnnlm-get-sampling-lm
%_bindir/rnnlm-get-word-embedding
%_bindir/rnnlm-sentence-probs
%_bindir/rnnlm-train
%_bindir/scale-post
%_bindir/select-feats
%_bindir/select-voiced-frames
%_bindir/shift-feats
%_bindir/show-alignments
%_bindir/show-transitions
%_bindir/splice-feats
%_bindir/subsample-feats
%_bindir/subset-feats
%_bindir/sum-lda-accs
%_bindir/sum-matrices
%_bindir/sum-mllt-accs
%_bindir/sum-post
%_bindir/sum-tree-stats
%_bindir/train-transitions
%_bindir/transcripts-to-fsts
%_bindir/transf-to-nnet
%_bindir/transform-feats
%_bindir/transform-vec
%_bindir/tree-info
%_bindir/vector-scale
%_bindir/vector-sum
%_bindir/wav-copy
%_bindir/wav-reverberate
%_bindir/wav-to-duration
%_bindir/weight-post
%_bindir/weight-silence-post

%changelog
* Thu Nov 06 2025 Ulysses Apokin <ulysses@altlinux.org> 5.5-alt1.gite02e35f
- Initial build for Sisyphus.
