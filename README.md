# AlphaOne

<p><strong>Động lực tạo ra project v&agrave; &yacute; tưởng ban đầu</strong></p>
<p>Trong v&agrave;i năm gần đ&acirc;y, ng&agrave;y c&agrave;ng nhiều dự &aacute;n giới thiệu &yacute; tưởng sử dụng Artificial Intelligence (AI) để học c&aacute;ch chơi c&aacute;c tr&ograve; chơi, thậm ch&iacute; l&agrave; thi đấu với con người. Nổi bật trong số đ&oacute; c&oacute; thể kể đến <strong>AlphaGO</strong>, một chương tr&igrave;nh của Google DeepMind kết hợp Supervised Learning v&agrave; Reinforcement Learning để học c&aacute;ch thi đấu cờ v&acirc;y v&agrave; đạt được những kết quả nhất định (xem th&ecirc;m tại <a href="https://deepmind.com/research/alphago/">đ&acirc;y</a>).&nbsp; Được gợi &yacute; từ <strong>AlphaGO</strong>, cũng như l&agrave; khao kh&aacute;t t&igrave;m hiểu khả năng vượt qua những giới hạn của con người bằng Artificial Intelligence, nh&oacute;m quyết định tạo ra một project về Reinforcement Learning &aacute;p dụng cho việc chơi c&aacute;c tr&ograve; chơi, với t&ecirc;n gọi l&agrave; <strong>AlphaOne</strong>.</p>
<p><strong>&Yacute; tưởng v&agrave; kế hoạch cụ thể</strong></p>
<ol>
<li>T&igrave;m kiếm c&aacute;c dự &aacute;n được implement bằng python cho game engine của Flappy Bird v&agrave; Gomoku, Mario.</li>
<li>T&igrave;m hiểu sơ qua về cấu tr&uacute;c code của c&aacute;c game engine n&oacute;i tr&ecirc;n (gi&uacute;p hiểu r&otilde; hơn).</li>
<li>Subproject 1 cho Flappy Bird: &Aacute;p dụng Reinforcement Learning ngay trong game engine để cải thiện khả năng chơi Flappy Bird của m&aacute;y qua nhiều lần chơi v&agrave; tự đ&aacute;nh gi&aacute;. Nh&oacute;m sẽ so s&aacute;nh kết quả thu được qua nhiều phi&ecirc;n bản kh&aacute;c nhau của thuật to&aacute;n.</li>
<li>Subproject 2 cho Flappy Bird: Sử dụng Convolutional Neural Network (CNN) để ph&acirc;n t&iacute;ch h&igrave;nh ảnh trước khi đưa ra h&agrave;nh động trong game, thay v&igrave; tận dụng engine c&oacute; sẵn.</li>
<li>Tương tự với Flappy Bird, &aacute;p dụng Reinforcement Learning cho 2 game Gomoku v&agrave; Mario.</li>
</ol>
<p>&nbsp;</p>
<p><strong>Th&ocirc;ng b&aacute;o cập nhật cho repository của dự &aacute;n</strong></p>
<p><strong>Flappy Bird</strong></p>
<p>Game engine nh&oacute;m sử dụng cho Flappy Bird được clone từ repository <a href="https://github.com/chncyhn/flappybird-qlearning-bot">n&agrave;y.</a></p>
<p>Trong repository của dự &aacute;n <strong>AlphaOne </strong>n&agrave;y, hai file định dạng .rar đ&atilde; được tải l&ecirc;n, bao gồm:</p>
<ul>
<li>flappybird-qlearning-bot_10by10.rar</li>
<li>flappybird-qlearning-bot_5by5.rar</li>
</ul>
<p>Th&ocirc;ng tin chi tiết:</p>
<p>Trong mỗi game, flappy bird của ch&uacute;ng ta quan s&aacute;t lại những trạng th&aacute;i m&agrave; n&oacute; từng đi qua, cũng như h&agrave;nh động được lựa chọn v&agrave;o thời điểm đ&oacute;. Mỗi cặp trạng th&aacute;i - h&agrave;nh động được đưa ra một mức thưởng/ phạt phụ thuộc v&agrave;o kết quả của cặp đ&oacute;. Sau khi chơi rất nhiều game, flappy bird c&oacute; thể đạt đến một số điểm kh&aacute; tốt.</p>
<p><span style="text-decoration: underline;">10 by 10</span></p>
<p>Đ&acirc;y l&agrave; phi&ecirc;n bản với c&aacute;c th&ocirc;ng số sau:</p>
<ul>
<li>Độ lớn grid để discretize state variables: 10 by 10</li>
<li>Learning Rate = 0.9</li>
<li>Discount = 0.6</li>
</ul>
<p><span style="text-decoration: underline;">5 by 5</span></p>
<p>Đ&acirc;y l&agrave; phi&ecirc;n bản với c&aacute;c th&ocirc;ng số sau:</p>
<ul>
<li>Độ lớn grid để discretize state variables: 5 by 5</li>
<li>Learning Rate = 0.9</li>
<li>Discount = 0.6</li>
</ul>
